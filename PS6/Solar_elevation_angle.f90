program solar_elevation_angle

use Declination_angle 
use Solar_hour_angle

implicit none

real, parameter :: p = 3.1415926536 
character(len=8) :: date
character(len=5) :: time
real :: lat,lon,h,sda
real :: sea
integer :: days

  write(*,*)"Input the date(YYYYMMDD):"
  read(*,*)date
  call declination(date)

  write(*,*)"Input the time(HH:MM):"
  read(*,*) time
  write(*,*)"Input the location:"
  write(*,*)"longitude:"
  read(*,*) lon
  write(*,*)"latitude:"
  read(*,*) lat
  call Sha(lon,days,time)

  sea = asin(sin(lat/180*p)*sin(sda/180*p)+cos(lat/180*p)*cos(sda/180*p)*cos(h/180*p))/p*180
  write(*,*) 'solar elevation angle is:',sea


end program Solar_elevation_angle
