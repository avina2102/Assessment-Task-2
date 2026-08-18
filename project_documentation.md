# Project Documentation

## Requirements Outline

### Defining the Purpose:
**The Need**- People spend a lot of time looking at their devices for too long without taking sufficient breaks. This way their eyes get harmed and also their body is not engaging in any sorts of physical activities and it could lead to long-term consequences for that person. They need some sort of robot or device letting them know when to take a break.

**Proposed Solutions** - I will design a robot that starts flashing a colour every hour so that people will be notified when to take a break from their screens so that they will stay healthy. This device will only work when it is turned on/connected to a power source so that it will not act as a distraction when it is not needed. It will flash bright blue every hour after it is turned on and the only way it will stop is if the person gets up and turns it off or restarts it.

### Identify Key Actions:
- Starts counting time the very second it gets plugged in or turned on to a power source, making sure it doesn't randomly go off when it's not needed
- Flashes a bright warning colour to force you to look away from your screen
- Forces you to physically get up out of your chair to either restart it or turn it off, which guarantees you are actually moving your body and taking a proper break
- Keeps your eyes and body healthy by repeating this loop every single hour, stopping you from getting long-term health problems from zero activity

### Functional Requirements:
**Power Input** - When the button is turned on, the microcontroller must immediately boot up, launch its internal clock code, and begin a 60-minute countdown loop in the background while keeping the LED turned off so it doesn't disturb you.

**Time Tracker** - The system must continuously calculate the total time elapsed since it was turned on, so that is knows when to start flashing the LED.

### Test Cases:
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Screentime too long after turned on           |The 1 hour timer goes off          |The light starts blinking                   |
|Screentime is adequate after turned on           |1 hour timer is counting down           |The system does not do anything                   |
|Product is not on           |There is no input           |There is no output                   |

### Non-Functional Requirements:
**Efficiency** - The system must be able to work as soon as it is turned on and must be able to countdown properly. The LED must be able to work properly and the user must also take responsibility to use the product for what it is meant for, only then the product will be able to reach maximum efficiency.

**Response Time** - The LED and Raspberry Pi Pico should activate to project light within one second after the timer is over. This way, the product will be can work like it is supposed to and the light will activate every hour.

**Accuracy** - The product must be accurate in terms of timing so that the light will activate at the correct time and the product will do what it is meant to do.

## Algorithms

### Flowchart 1:
![1787040977021](image/project_documentation/1787040977021.png)

### Flowchart 2:
![1787041429567](image/project_documentation/1787041429567.png)

### Flowchart 3:
![1787045075205](image/project_documentation/1787045075205.png)

### Pseudocode 1:
![1787044068467](image/project_documentation/1787044068467.png)

### Pseudocode 2:
![alt text](image-4.png)

### Pseudocode 3:
![1787044197058](image/project_documentation/1787044197058.png)

## Development and Integration

### Final Code (after I changed my idea a bit)
For my circuit to work and not overcomplicate it, I had to remove the alarm aspect of my machine and change my Requirements Outline, circuit setup, flowcharts, pseudocodes and main code for it to fit my new idea.
![1787045418742](image/project_documentation/1787045418742.png)

## Testing and Debugging

### Test Cases:
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Screentime too long after turned on           |The 1 hour timer goes off          |The light starts blinking                   |
|Screentime is adequate after turned on           |1 hour timer is counting down           |The system does not do anything                   |
|Product is not on           |There is no input           |There is no output                   |

For this test case, I do not need to make much improvements, as it aligns with my system and the code well. This is because I had to simplify my test case a little, to match the rest of my project. So the improvements I made were directed towards the Test Case itself rather than the code, circuit, etc.

### First code draft:
![1787038006712](image/project_documentation/1787038006712.png)

### Second code draft:
![1787040121207](image/project_documentation/1787040121207.png)

### Final code:
![1787045418742](image/project_documentation/1787045418742.png)

### Evaluate Process:

In the original test case, I had included a buzzer to alarm the users to take a break from their screens. But eventually, I realised that for some reason my buzzer wasn't working and I decided to use the component that was already working instead of overcomplicating my project into something that doesn't work at all in the end. To fix errors, I analysed my code to see whether the LED values, pin values and everything was all correct. When I found an error I tried fixing it and if it didn't work, I repeated the process. The LED component went really well, because the circuit was quite simple to make and also the code was not too hard to work either. What really challenged me through this process was my initial idea to include the piezzo buzzer to make an alarming noise to notify the users. Even though I connected it into the circuit, the code just never worked. When I searched up what the problem was, it turned out that my piezzo buzzer was most likely inactive. So I decided to drop this aspect and keep my project simple. Based on the test results, I think my system might be a little simple and it may not showcase my full capacity that well, so I could have improved the machine to be a little more interesting.    

## Evaluation

### PMI Table - Rachael
| Plus | Minus     | Interesting   |
|---------- |---------- |----------------   |
|       |            |            |

### PMI Table Sarah
| Plus | Minus     | Implication   |
|---------- |---------- |----------------   |
|       |            |            |

### Final Evaluation Questions (SEEL)
**Evaluate your Final Test in Relation to Functional Criteria:**


**Evaluate your Final Test in Relation to Non-Functional Criteria:**

**Evaluate your Final Performance in Relation to the Identified Need:**
My product's final performance

**Evaluate your Project in Relation to Project Management:**

**Evaluate your Project in Relation to Peer Feedback:**

**Justify Future Improvements you could make to your Final Product:**