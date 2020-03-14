/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int main()
{
    int day, month, year, dayoftheweek, indexMonth, indexYear;
    printf("Input day, month and year: ");
    scanf("%ld %ld %ld", &day, &month, &year);
        if (((month == 3)||(month == 11))&&(year>=0)&&(year<=20)) //2,3,11 21 век просто

    { indexMonth =4;
    indexYear=(6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if (((month == 3)||(month == 11))&&(year>=21)&&(year<=99)) //2,3,11 20 век просто

    { indexMonth =4;
    indexYear=( year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
        
        
        
        if (((month == 1)||(month == 10))&&(year>=0)&&(year<=20)) //2,3,11 21 век просто
    { indexMonth =1;
    indexYear=(6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if (((month == 1)||(month == 10))&&(year>=21)&&(year<=99)) //2,3,11 20 век просто
     {   
         indexMonth =1;
         indexYear=( year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
     }
     
     if (((month == 4)||(month == 7))&&(year>=0)&&(year<=20))
    { indexMonth =0;
    indexYear=(6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if (((month == 4)||(month == 7))&&(year>=21)&&(year<=99))
    { indexMonth =0;
    indexYear=( year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
     if (((month == 9)||(month == 12))&&(year>=21)&&(year<=99))
    { indexMonth =6;
    indexYear=( year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if (((month == 9)||(month == 12))&&(year>=0)&&(year<=20))
    { indexMonth =6;
    indexYear=( 6+ year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
     if ((month == 5)&&(year>=0)&&(year<=20))
    { indexMonth =2;
    indexYear=( 6+ year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if ((month == 5)&&(year>=21)&&(year<=99))
    { indexMonth =2;
    indexYear=(  year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
        }
     if ((month == 6)&&(year>=21)&&(year<=99)) 
    { indexMonth =5;
    indexYear=(  year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if ((month == 6)&&(year>=0)&&(year<=20)) 
    { indexMonth =5;
    indexYear=( 6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
     if ((month == 8)&&(year>=0)&&(year<=20)) 
    {indexMonth=3;
    indexYear=( 6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if ((month == 8)&&(year>=21)&&(year<=99)) 
    {indexMonth=3;
    indexYear=(  year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    
    
    
    if ((month == 2)&&(year%4 == 0)&&(year>=0)&&(year<=20)) // Февраль висок год 21 век
    { indexMonth=4;
    indexYear=(6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear -1)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
     else if ((month == 2)&&(year%4 == 0)&&(year>=21)&&(year<=99)) // Февраль висок 20 век
     {indexMonth=4;
    indexYear=( year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear -1)%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}}
     
     if ((month == 2)&&(year%4!= 0)&&(year>=0)&&(year<=20)) // Февраль висок год 21 век
    { indexMonth=4;
    indexYear=(6 + year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear )%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}
    }
    else if ((month == 2)&&(year%4!= 0)&&(year>=21)&&(year<=99)) // Февраль висок 20 век
     {indexMonth=4;
    indexYear=( year +year/4)%7;
    dayoftheweek=(day + indexMonth + indexYear )%7;
     if(dayoftheweek==2)
     {printf("It's Monday!");}
     if(dayoftheweek==3)
     {printf("It's Tuesday!");}
     if(dayoftheweek==4)
     {printf("It's Wednesday!");}
     if(dayoftheweek==5)
     {printf("It's Thursday!");}
     if(dayoftheweek==6)
     {printf("It's Friday!");}
     if(dayoftheweek==0)
     {printf("It's Saturday!");}
     if(dayoftheweek==1)
     {printf("It's Sunday!");}}
     
     }
