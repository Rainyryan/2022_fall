#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

int main (void) {
   long long tosses, hits;
   int id;
   int size;
   MPI_Init(NULL, NULL);
   MPI_Comm_rank(MPI_COMM_WORLD, &id);
   MPI_Comm_size(MPI_COMM_WORLD, &size);
   double actual_pi = 3.14159265358979323;

   if(!id){
      printf("Enter number of tosses:\n");
      scanf("%lld", &tosses);
   }
   double startTime = 0.0, totalTime = 0.0;
   //n = next power of 2 of size
   int n = size;
   n--; 
   n |= n >> 1;
   n |= n >> 2;
   n |= n >> 4;
   n |= n >> 8;
   n |= n >> 16;
   n++;
   //tree-structured broadcast
   while(n>1){
      if(!(id%n)){
         if(id+n/2 < size) MPI_Send(&tosses, 1, MPI_LONG_LONG, id+n/2, n, MPI_COMM_WORLD);
      }else if(!(id%(n/2))){
         MPI_Recv(&tosses, 1, MPI_LONG_LONG, id-n/2, n, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
         //printf("process %2d recieved tosses %lld\n", id, tosses);
      }
      n >>= 1;
   }
   startTime = MPI_Wtime(); 
   //Monte Carlo
   hits = 0;
   long loc_toss = tosses / size;
   double pi_estimate, x, y, d_squared;
   srand(time(NULL)+id*rand());
   for (long toss = 0; toss < loc_toss; toss++){
      x = (double)rand()/(double)RAND_MAX;
      y = (double)rand()/(double)RAND_MAX;
      d_squared = x*x + y*y;
      if (d_squared <= 1) ++hits;
   }
   pi_estimate = 4 * (double)hits/((double)loc_toss);
   totalTime = MPI_Wtime() - startTime;
   printf("%2d)hits %lld, pi_estimate %lf, took %lf secs.\n", id, hits, pi_estimate, totalTime);
   //tree-structured reduce (sum)
   int i = id, l = 1;
   long long totalhits = hits;
   while(1){
      if(i%2){
         MPI_Send(&totalhits, 1, MPI_INT, id-l, l, MPI_COMM_WORLD);
         break;
      }else if(id+l<size){
         MPI_Recv(&hits, 1, MPI_INT, id+l, l, MPI_COMM_WORLD, MPI_STATUS_IGNORE);      
         totalhits += hits;
      }else if(!id){
         pi_estimate = 4 * (double)totalhits/((double)tosses);
         totalTime = MPI_Wtime() - startTime;
         printf("\n%2d)totalhits %lld from %lld tosses, pi_estimate %lf\n", id, totalhits, tosses, pi_estimate);
         printf("The error is about %lf, took %lf secs.\n\n", actual_pi-pi_estimate > 0? actual_pi-pi_estimate:pi_estimate-actual_pi, totalTime);
         break;
      }
      i >>= 1;
      l <<= 1;
   }
   MPI_Finalize();
   return 0;
}