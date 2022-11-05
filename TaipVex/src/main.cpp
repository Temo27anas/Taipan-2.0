/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       C:\Users\Anas                                             */
/*    Created:      Sat Nov 05 2022                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Motor1               motor         1               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();


  char var=0;
  double dist=0;
 Motor1.resetRotation();
  
  while(1){
    
    scanf("%c",&var);

    if(var=='o'){
    Motor1.spin(forward);
  
    //Brain.Screen.print("up");
    //Brain.Screen.newLine();
    
    wait(0.11,sec);
    Motor1.stop();  
    var = 0;
    
    }
   
    else if(var=='l'){
    
    Motor1.spin(reverse);

    //Brain.Screen.print("down");
    //Brain.Screen.newLine(); 
    
    wait(0.11,sec);
    Motor1.stop();  
    var = 0;
    }


  //update distance

  dist = Motor1.rotation(deg)*4/360;

    Brain.Screen.print("%f",dist);
    Brain.Screen.newLine(); 
  
  

    
  }
  

  
  
}
