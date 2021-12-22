module Constants
implicit none

 contains

 subroutine Matrix_multip(M,N,MN)
 implicit none
 
 real :: M(5,3),N(3,5),MN(5,5)
 MN = matmul(M,N)

 end subroutine Matrix_multip

end module Constants
