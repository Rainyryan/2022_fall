/* circuitSatifiability.c solves the Circuit Satisfiability
 *  Problem using a brute-force sequential solution.
 *
 *   The particular circuit being tested is "wired" into the
 *   logic of function 'checkCircuit'. All combinations of
 *   inputs that satisfy the circuit are printed.
 *
 *   16-bit version by Michael J. Quinn, Sept 2002.
 *   Extended to 32 bits by Joel C. Adams, Sept 2013.
 */

#include <stdio.h>     // printf()
#include <limits.h>    // UINT_MAX
#include <mpi.h>

int checkCircuit (int, int);

int main (void) {
   int id;           /* process id */
   int count = 0;        /* number of solutions */
   
   int size, totalcount = 0;
   double startTime = 0.0, totalTime = 0.0; 
   MPI_Init(NULL, NULL);
   MPI_Comm_rank(MPI_COMM_WORLD, &id);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   int w = USHRT_MAX/size;
   int s = w * id;

   startTime = MPI_Wtime();
   for (int i = s; i < s+w; i++) { 
      count += checkCircuit(id, i); 
   }
   totalTime = MPI_Wtime() - startTime; 
   printf("Process %d finished in time %f secs. %d local solutions found.\n", id, totalTime, count); 
   fflush (stdout);

   //tree-structured sum
   int i = id, l = 1;
   totalcount = count;
   while(1){
      if(i%2){
         MPI_Send(&totalcount, 1, MPI_INT, id-l, l, MPI_COMM_WORLD);
         break;
      }else if(id+l<size){
         MPI_Recv(&count, 1, MPI_INT, id+l, l, MPI_COMM_WORLD, MPI_STATUS_IGNORE);      
         totalcount += count;
      }else if(!id){
         printf("\nA total of %d solutions were found.\n\n", totalcount);
         break;
      }
      i >>= 1;
      l <<= 1;
   }

   MPI_Finalize();
   return 0;
}

/* EXTRACT_BIT is a macro that extracts the ith bit of number n.
 *
 * parameters: n, a number;
 *             i, the position of the bit we want to know.
 *
 * return: 1 if 'i'th bit of 'n' is 1; 0 otherwise 
 */

#define EXTRACT_BIT(n,i) ( (n & (1<<i) ) ? 1 : 0)


/* checkCircuit() checks the circuit for a given input.
 * parameters: id, the id of the process checking;
 *             bits, the (long) rep. of the input being checked.
 *
 * output: the binary rep. of bits if the circuit outputs 1
 * return: 1 if the circuit outputs 1; 0 otherwise.
 */

#define SIZE 16

int checkCircuit (int id, int bits) {
   int v[SIZE];        /* Each element is a bit of bits */
   int i;

   for (i = 0; i < SIZE; i++)
     v[i] = EXTRACT_BIT(bits,i);

   if (  (v[0] || v[1]) && (!v[1] || !v[3]) && (v[2] || v[3])
       && (!v[3] || !v[4]) && (v[4] || !v[5])
       && (v[5] || !v[6]) && (v[5] || v[6])
       && (v[6] || !v[15]) && (v[7] || !v[8])
       && (!v[7] || !v[13]) && (v[8] || v[9])
       && (v[8] || !v[9]) && (!v[9] || !v[10])
       && (v[9] || v[11]) && (v[10] || v[11])
       && (v[12] || v[13]) && (v[13] || !v[14])
       && (v[14] || v[15])  )
   {
      printf ("%d) %d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d \n", id,
         v[15],v[14],v[13],v[12],
         v[11],v[10],v[9],v[8],v[7],v[6],v[5],v[4],v[3],v[2],v[1],v[0]);
      fflush (stdout);
      return 1;
   } else {
      return 0;
   }
}

