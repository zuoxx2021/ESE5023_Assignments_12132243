module Solar_hour_angle  

implicit none 

  real, parameter :: pi = 3.1415926536   
   
contains      

  subroutine Sha(lon,days,time)          
    
    integer :: hour,minute
    integer,intent(in) :: days
    real,intent(in) :: lon
    real :: hours,gama,eot,offset,LST,dtz,LST1
    real :: h
    character(len=5),intent(in) :: time

    common h
    
    read(time(1:2),*) hour
    read(time(4:5),*) minute

    LST = hour+minute*1.0/60

    gama = 2*pi/365*(days-1+(LST-12)/24)
    eot = 229.18*(0.000075+0.001868*cos(gama)-0.032077*sin(gama)- 0.014615*cos(2*gama)- 0.40849*sin(2*gama))
    dtz = ceiling((lon-7.5)/15)
    offset = eot+4*(lon-15*dtz)
    LST1 = LST+offset/60

    ! LST in hour
    h = 15*(LST1-12)
    write(*,*) 'solar hour angle is',h
    !write(*,*) 'eot is',eot
    !write(*,*) 'offset and is',offset
    !write(*,*) 'dtz is',dtz
    !write(*,*) 'lst:', LST1

  end subroutine Sha 
   
end module Solar_hour_angle

