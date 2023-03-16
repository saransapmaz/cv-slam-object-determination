#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>
#include <geometry_msgs/Twist.h>

int motor1pin1 = 2;
int motor1pin2 = 3;

int motor2pin1 = 4;
int motor2pin2 = 5;
ros::NodeHandle  nh;

void messageCb(const geometry_msgs::Twist &msg){

  float x = msg.linear.x;
  float z = msg.angular.z;
  if(x > 0.0 )
  {
    ileri_git();
  }
  if(z > 0.0)
  {
    sag_don();
  }
  if(z< 0.0)
  {
    sol_don();
  }
  if (x==0.0 && z==0.0)
  {
    dur();
  }
}

void ileri_git()
{
  analogWrite(9, 100);
  analogWrite(10, 100);
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
}

void sag_don()
{
  analogWrite(9, 100);
  analogWrite(10, 100);
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);
}
void sol_don()
{
  analogWrite(9, 100);
  analogWrite(10, 100);
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
}

void dur(){
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, LOW);
}
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb );
bool _connected = false;

void setup()
{ 
  Serial.begin(57600);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  pinMode(9, OUTPUT); 
  pinMode(10, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  if (!rosConnected())
  {
    stop();}
  nh.spinOnce();
}

bool rosConnected()
{
  // If value changes, notify via LED and console.
  bool connected = nh.connected();
  if (_connected != connected)
  {
    _connected = connected;
    digitalWrite(LED_BUILTIN, !connected); // false -> on, true -> off
    Serial.println(connected ? "ROS connected" : "ROS disconnected");
  }
  return connected;
}

void stop(){
  Serial.println("dur");
}

