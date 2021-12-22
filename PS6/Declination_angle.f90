module Declination_angle
implicit none

real, parameter :: pi = 3.1415926536  

contains
 
 subroutine declination(date)

  character (len=8),intent(in) :: date
  integer :: year,month,day
  integer :: days
  real :: sda
  integer :: dayofmonth(12)=[31,28,31,30,31,30,31,31,30,31,30,31]
  
  common days,sda

 ! write(*,*)"Input the date(YYYYMMDD):"
 ! read(*,*)date

  read(date(1:4),*) year
  read(date(5:6),*) month
  read(date(7:8),*) day

  ! 判断是否闰年
  if(((MOD(year,4)==0).and.(MOD(year,100)/=0)).or.(mod(year,400)==0)) then
    dayofmonth(2)=29
  else
    dayofmonth(2)=28
  end if

  ! 计算天数
  days=sum(dayofmonth(1:month-1))+day

  ! 计算declination angle
  sda = asin(sin(-23.44*pi/180)*cos((360/365.24*(Days+10)+360/pi*0.0167*sin((360/365.24*(Days-2))*pi/180))*pi/180))/pi*180

  ! write(*,*)'solar declination is:',sda

 end subroutine declination

!  real function 


end module Declination_angle
