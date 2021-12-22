program main

use Constants

implicit none

  real :: M(5,3),N(3,5),MN(5,5)

  ! opening file and reading
  open(1, file = 'M.dat')
  read(1,*), M
  close(1)  
  
  open(2, file = 'N.dat')
  read(2,*), N
  close(2)

  call Matrix_multip(M,N,MN)

  open(unit=3, file='MN.dat')
  write(3,'(f9.2)'), MN
  close(3) 

end program main

!--------------------------------------

