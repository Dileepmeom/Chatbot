<!-- image -->

## Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

Instructional Booklet

| Description                                                 |   Page |
|-------------------------------------------------------------|--------|
| 1. Introduction . . . . . . . . . . . . . . . . . . . . . . |      2 |
| 2. Hardware Description . . . . . . . . . . . . . . .       |      7 |
| 3. Operator Panel . . . . . . . . . . . . . . . . . . . .   |     11 |
| 4. Operation. . . . . . . . . . . . . . . . . . . . . . . . |     14 |
| 5. Programming . . . . . . . . . . . . . . . . . . . . .    |     19 |
| 6. Troubleshooting and Maintenance . . . . . . .            |     22 |
| Appendix A: Status Display Messages . . . .                 |     27 |
| Appendix B: Historical Display Information .                |     28 |
| Appendix C: Time/Date Display Information                   |     30 |
| Appendix D: ATC-600 Menu Tree . . . . . .                   |     31 |
| Appendix E: Operational Flowcharts . . . . .                |     33 |

<!-- image -->

For more information visit: www.eaton.com

<!-- PAGE 1 END -->

Page 2

Effective: March 2010

<!-- image -->

THE ATC-600 IS FACTORY PROGRAMMED FOR A SPECIFIC TRANSFER SWITCH. DO NOT ATTEMPT TO INTERCHANGE ATC-600 CONTROL DEVICES WITHOUT CONSULTING THE FACTORY.

All possible contingencies which may arise during installation, operation, or maintenance, and all details and variations of this equipment do not purport to be covered by these instructions. If further information is desired by purchaser regarding his particular installation, operation or maintenance of his equipment, the local Eaton representative should be contacted.

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Section 1: Introduction

## 1.1  Preliminary Comments and Safety Precautions

This technical document is intended to cover most aspects associated with the installation, application, operation and maintenance of the ATC-600. It is provided as a guide for authorized and qualified personnel only in the selection and application of the ATC600. Please refer to the specific WARNING and CAUTION in Section 1.1.2 before proceeding. If further information is required by the purchaser regarding a particular installation, application or maintenance activity, a Eaton representative should be contacted.

## NOTICE

DURING CONVERSATIONS WITH EATON CONCERNING TROUBLESHOOTING OR PRODUCT RETURN, THE CUSTOMER MAY BE ASKED FOR INFORMATION PERTAINING TO THE SOFTWARE VERSION AND OPTIONS INCLUDED IN THE SPECIFIC UNIT. REFER TO THE 'NOTE' UNDER THE TOPIC 'HELP PUSHBUTTON' IN PARAGRAPH 3.4 FOR INSTRUCTIONS ON HOW TO OBTAIN THIS INFORMATION.

## 1.1.1  Warranty and Liability Information

NO WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE OF MERCHANTABILITY, OR WARRANTIES ARISING FROM COURSE OF DEALING OR USAGE OF TRADE, ARE MADE REGARDING THE INFORMATION, RECOMMENDATIONS AND DESCRIPTIONS CONTAINED HEREIN. In no event will Eaton be responsible to the purchaser or user in contract, in tort (including negligence), strict liability or otherwise for any special, indirect, incidental or consequential damage or loss whatsoever, including but not limited to damage or loss of use of equipment, plant or power system, cost of capital, loss of power, additional expenses in the use of existing power facilities, or claims against the purchaser or user by its customers resulting from the use of the information and descriptions contained herein.

## 1.1.2  Safety Precautions

All safety codes, safety standards and/or regulations must be strictly observed in the installation, operation and maintenance of this device.

<!-- image -->

THE WARNINGS AND CAUTIONS INCLUDED AS PART OF THE PROCEDURAL STEPS IN THIS DOCUMENT ARE FOR PERSONNEL SAFETY AND PROTECTION OF EQUIPMENT FROM DAMAGE. AN EXAMPLE OF A TYPICAL WARNING LABEL HEADING IS SHOWN IN REVERSE TYPE TO FAMILIARIZE PERSONNEL WITH THE STYLE OF PRESENTATION. THIS WILL HELP TO INSURE THAT PERSONNEL ARE ALERT TO WARNINGS, WHICH MAY APPEAR THROUGHOUT THE DOCUMENT. IN ADDITION, CAUTIONS ARE ALL UPPER CASE AND BOLDFACE AS SHOWN BELOW.

<!-- image -->

## CAUTION

COMPLETELY READ AND UNDERSTAND THE MATERIAL PRESENTED IN THIS DOCUMENT BEFORE ATTEMPTING INSTALLATION, OPERATION OR APPLICATION OF THE EQUIPMENT. IN ADDITION, ONLY QUALIFIED PERSONS SHOULD BE PERMITTED TO PERFORM ANY WORK ASSOCIATED WITH THE EQUIPMENT. ANY WIRING INSTRUCTIONS PRESENTED IN THIS DOCUMENT MUST BE FOLLOWED PRECISELY. FAILURE TO DO SO COULD CAUSE PERMANENT EQUIPMENT DAMAGE.

For more information visit: www.eaton.com

<!-- PAGE 2 END -->

<!-- image -->

## Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## 1.2  Background

Transfer switches are used to protect critical electrical loads against loss of power. The load's normal power source is backed up by a secondary (emergency) power source. A transfer switch is connected to both the normal and emergency sources and supplies the load with power from one of these two sources. In the event that power is lost from the normal source, the transfer switch transfers the load to the secondary source. Transfer can be automatic or manual, depending upon the type of transfer switch equipment being used. Once normal power is restored, the load is transferred back to the normal power source.

In automatic transfer switch equipment, the switch's intelligence system initiates the transfer when normal power fails or falls below a preset voltage. If the emergency source is a standby generator, the transfer switch initiates generator starting and transfers to the emergency source when sufficient generator voltage is available. When normal power is restored, the transfer switch automatically transfers back and initiates engine shutdown.

An automatic transfer switch consists of three basic elements:

1. Main contacts to connect and disconnect the load to and from the source of power
2. A transfer mechanism to affect the transfer of the main contacts from source to source
3. Intelligence/supervisory circuits to constantly monitor the condition of the power sources and thus provide the intelligence necessary for the switch and related circuit operation

This manual deals with the third basic element of the automatic transfer switch, the required intelligence/ supervisory circuits. Prior to the introduction of ATC-600, this function was performed by a door mounted logic panel. The logic panel could be the relay logic type or the solid state logic type. In either case, the panel consisted of a number of individually mounted and wired devices offering a limited amount of system flexibility, especially in the case of the relay logic design. ATC-600 brings intelligence, supervisory and programming capabilities, never before available, to automatic transfer switch equipment.

## 1.3  Product Overview

The ATC-600 is a comprehensive, multi-function, microprocessor based automatic transfer switch controller. It is a compact, selfcontained, panel mounted device designed to replace traditional relay and solid state logic panels (Figures 1 and 2 ).

Designed to meet the needs of markets worldwide, ATC-600:

- Is a UL Recognized Component
- Meets Seismic Requirements of Uniform and California Building Codes (exceeding requirements of worst case Zone 4 levels)
- Complies with UL 991 environmental tests
- Complies with IEC 61000-4-2, 61000-4-3, 61000-4-4, and 61000-4-5
- Complies with CISPR 11, Class A
- Complies with FCC Part 15, Subpart B, Class A

ATC-600 provides an unmatched degree of programmed flexibility to address the needs of any system. It operates from most system voltages available worldwide at 50 or 60 Hertz. In addition, a period of no control power operation is provided. ATC-600 monitors the condition of the 3-phase line-to-line voltage and frequency of both the Normal and Emergency sources. It can also be programmed for single phase operation. ATC-600 provides the necessary intelligence to insure that the switch operates properly through a series of programmed sensing and timing functions.

A standard ATC-600 will:

- Monitor Normal and Emergency source voltages and frequencies
- Provide undervoltage monitoring of Normal and Emergency sources
- Permit customer programming
- Display real time and historical information
- Permit system testing
- Offer Help Screen assistance
- Store customer/factory established parameters in nonvolatile memory
- Communicate using a PONI
- Provide faceplate source/load status indications

A wide array of additional features are available to address the most sophisticated system requirements, such as:

- Previously unavailable Load Monitoring and Delayed Transition
- In-phase Transition

## 1.4  Functions/Features/Options

The primary function of ATC-600 is to accurately monitor power sources and provide the necessary intelligence to operate a transfer switch in an appropriate and timely manner. In addition, ATC-600 provides useful present and historical data, reliable twoway communications, and programming through the device's faceplate or communications option. ATC-600 features proprietary microprocessor technology to provide and maintain superior precision and versatility during both programming and data access.

## 1.4.1  Operational Simplicity

From installation to programming to usage, ATC-600 was designed with operational simplicity in mind. Only one style needs to be considered, regardless of input/output requirements or system voltages and frequencies. ATC-600 provides the functionality of numerous other devices combined in one package that mounts in less than 7 by 11 inches of panel space.

The user friendly front panel interface simplifies routine operation, programming, data presentation and setting adjustments. An LED based display provides the flexibility of large character displays for enhanced visibility. The operation of front panel membrane pushbuttons moves the ATC-600 display from function to function or step to step within a function. Three LEDs at the top of the faceplate provide an immediate indication as to the device's operational mode. An integral Help Mode provides immediate user assistance in the form of English language message displays through the use of a front panel Help pushbutton.

With a P roduct O perated N etwork I nterface (PONI), the ATC-600 is communications ready and compatible with other devices in the IQ Family of products. The Communication Module (PONI) is available in three versions, the INCOM PONI, RS-232 PONI and PONI Modem. Reliable two-way communications can be provided over a twisted pair communications network. With the INCOM PONI, ATC-600 is compatible with the Eaton IMPACC system.

## 1.4.2  Standard and Optional Features

A variety of programmable features are available to meet a wide variety of application requirements. Individual features or feature combinations provide the intelligence required to tailor switches to individual needs.

Effective: March 2010

<!-- PAGE 3 END -->

Page 4

Effective: March 2010

The features are factory activated, depending upon customer requirements. The specific variable setpoints associated with standard and factory activated features are stored in a nonvolatile memory. Activated feature setpoints are available for customer adjustment. Any feature not selected and factory activated cannot be viewed or adjusted.

## NOTICE

WITH RESPECT TO THEIR USE IN THIS DOCUMENT AND AS THEY RELATE TO AUTOMATIC TRANSFER SWITCH OPERATION, THE FOLLOWING WORDS OR PHRASES ARE DEFINED:

## Available

A source is defined as available when it is within its undervoltage/ overvoltage/underfrequency/overfrequency (if applicable) setpoint ranges for the nominal voltage and frequency setting.

## Fails

A source is defined as failed when it is outside of its undervoltage/ overvoltage/underfrequency/overfrequency (if applicable) setpoint ranges for the nominal voltage and frequency setting.

## Normal Source

The Normal Source is defined as the source that is preferred. The Preferred Source setting allows the operator to select Source 1, Source 2 or NONE as the Preferred Source. If NONE is chosen, the Preferred Source or the Normal Source will be the source that is presently attached to the load. If the Preferred Source feature is not available from the factory, the default is set as being Source 1 as the Preferred and Normal Source.

## Emergency Source

The Emergency Source is defined as the source that is not preferred. If NONE is chosen for the Preferred Source setting, the Emergency Source will be the source that is presently not attached to the load. Therefore, in this condition after a transfer, what was the Normal and Emergency Sources will switch between Source 1 and 2. If the Preferred Source feature is not available from the factory, the default is set with Source 2 as the Emergency Source.

## Option #

For personnel who are familiar with previous transfer switch controller option specifications, an attempt at equivalence to some of the features is made.

ATC-600 features with a brief description follow.  The actual programmable setpoints for each feature are covered in Section 5.

## Standard Feature:  Time Delay Engine Start (TDES)

TDES is used where the source is an engine generator. It delays initiation of the engine start circuit in order to override momentary power outages and/or fluctuations. This timer and the associated engine start circuit will operate with or without control power. There are two separate start circuits, one for each source when applications of two generators are selected, although the same TDES timer value is used for both. When one generator is selected, this timer's engine start circuit will operate on generator 2 for source 2. If the source that is being transferred to has a generator and that source is already available, the TDES timer is bypassed.

## Standard Feature:  Time Delay Normal to Emergency (TDNE)

<!-- image -->

## Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Standard Feature:  Time Delay Emergency to Normal (TDEN)

TDEN delays the transfer to the Normal Source to permit stabilization of the Normal power source before the transfer is made. This timer will begin the countdown from its setting value when the Normal Source becomes available. During the countdown of this timer, if the Normal Source should become unavailable, the timer will be aborted. If the Preferred Source is available and the Emergency Source fails while the TDEN timer is counting down, the TDEN timer will be bypassed.

## Standard Feature:  Time Delay for Engine Cool-Off (TDEC)

TDEC permits the generator to run under a no-load condition after a transfer from the generator source has been made. Countdown timing begins when the transfer is completed. In applications where two generators are selected, the same cool-off timer setting value is used for both.

## Standard Feature:  Time Delay Emergency Failure (TDEF)

TDEF is used where at least one source is an engine generator. TDEF will delay an available source from being declared unavailable in order to override momentary generator fluctuations. This time delay is only implemented when the load is connected to a generator source. TDEF is not displayed when the number of generators is zero.

<!-- image -->

CHANGING THE SYSTEM NOMINAL VOLTAGE OR FREQUENCY SETPOINTS WILL CAUSE PICKUP AND DROPOUT SETPOINTS TO CHANGE AUTOMATICALLY TO NEW DEFAULT VALUES.

## Standard Feature :  System Nominal Frequency (NOMF)

There are only two choices for system nominal frequency of the distribution system, 50 or 60 Hertz. The dropout/pickup, underfrequency and overfrequency upper and lower setting limits are based on the nominal frequency value.

## Standard Feature:  System Nominal Voltage (NOMV)

This refers to the standard system nominal RMS line to line voltage. A wide range (120 to 600) of sensing voltage is available to be programmed. The dropout/pickup, undervoltage and overvoltage upper and lower setting limits are based upon the nominal voltage value.

## Standard Feature:  Undervoltage Monitoring for Source 1 (1UVD, 1UVP)

This feature constantly monitors Source 1 for an undervoltage condition. When the Source 1 voltage drops to a value equal to or below the undervoltage dropout setting, the source will become unavailable. The source's voltage will then have to rise to a value that is equal to or above the pickup setting to become available again.

## Standard Feature:  Undervoltage Monitoring for Source 2 (2UVD, 2UVP)

This feature functions the same as Standard Feature (1UVD, 1UVP), except for Source 2 instead of Source 1.

## Standard Feature:  Underfrequency Monitoring for Source 2 (2UFD, 2UFP)

This feature functions the same as Optional Feature 26E, except for Source 2 instead of Source 1.

TDNE delays the transfer to the Emergency Source to permit stabilization of the Emergency power source before the transfer is made. This timer will begin the countdown from its setting value when the Emergency Source becomes available. If the Normal Source should become available during the countdown of this timer, the timer will be aborted.

For more information visit: www.eaton.com

<!-- PAGE 4 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Standard Feature:  Commit to Transfer During TDNE Timing (CTDNE)

This feature provides for selection as to whether or not commitment to transfer is desired when Time Delay Normal to Emergency countdown has begun.  If no commitment is chosen and the Normal Source returns to availability when the TDNE timer is counting down, the transfer is aborted and the engine generator (if applicable) is cooled down.

## Standard Feature:  Engine Test Mode (TMODE)

This feature provides selection of the type of test that can be initiated by the front panel Engine Test pushbutton. An engine test without transferring the load to it, or an engine test with a full transfer of the load to the engine can be chosen. Load testing is fail-safe. If the generator fails during testing for any reason, the ATC-600 will signal the transfer switch to return to normal. If disable test mode is chosen, the front panel pushbutton cannot be used to initiate a test.

## Standard Feature:  Test Engine Run (TER)

This feature provides selection of the length of time in hours and minutes that the ATC-600 will enable the generator contacts during an Engine Test that was initiated from the front panel pushbutton or for the plant exerciser feature, if applicable.

## Standard Feature 5C:  Overfrequency Monitoring for Source 2 (2OFD, 2OFP)

This feature constantly monitors Source 2 for an overfrequency condition. When the Source 2 frequency rises to a value equal to or above the overfrequency dropout setting, the source will become unavailable. The source's frequency will then have to drop to a value that is equal to or below the pickup setting to become available again.

## Standard Feature 5E:  Overvoltage Monitoring for Source 2 (2OVD, 2OVP)

This feature constantly monitors Source 2 for an overvoltage condition. When the Source 2 voltage rises to a value equal to or above the overvoltage dropout setting, the source will become unavailable. The source's voltage will then have to drop to a value that is equal to or below the pickup setting to become available again.

## Standard Feature 8C/8D:  Transfer Time Delay Bypass

This feature allows an external pushbutton input to be used to bypass the timer for Standard Feature (TDNE) or Standard Feature (TDEN) individually, or both simultaneously. This feature is usually used in testing when it is not desirable to wait for completion of the timing sequence.

## Standard Feature 23:  Plant Exerciser (EXER)

This feature provides for the automatic test operation of the generator for a pre-selected weekly interval. When the test is running, pressing and releasing the Engine Test pushbutton will cancel the test. The day of the week, hour, and minute that exercising is desired can be programmed into the ATC-600. The type of test, whether a load transfer or just an engine test, can also be selected. Load testing is fail-safe. If the generator fails during testing for any reason, the ATC-600 will signal the transfer switch to return to normal.

## Standard Feature 26C:  Overvoltage Monitoring for Source 1 (1OVD, 1OVP)

This feature constantly monitors Source 1 for an overvoltage condition. When the Source 1 voltage rises to a value equal to or above the overvoltage dropout setting, the source will become unavailable. The source's voltage will then have to drop to a value that is equal to or below the pickup setting to become available again.

Effective: March 2010

## Standard Feature 26D:  Go To Emergency

This feature enables an external contact closure to initiate a transfer from the Normal Source to the Emergency Source.  If the external contact is closed and the Emergency Source fails, the ATC-600 will transfer the load back to the Normal Source.

## Standard Feature 26E:  Underfrequency Monitoring for Source 1 (1UFD, 1UFP)

This feature constantly monitors Source 1 for an underfrequency condition. When the Source 1 frequency drops to a value equal to or below the underfrequency dropout setting, the source will become unavailable. The source's frequency will then have to rise to a value that is equal to or above the pickup setting to become available again.

## Standard Feature 26F:  Overfrequency Monitoring for Source 1 (1OFD, 1OFP)

This feature constantly monitors Source 1 for an overfrequency condition. When the Source 1 frequency rises to a value equal to or above the overfrequency dropout setting, the source will become unavailable. The source's frequency will then have to drop to a value that is equal to or below the pickup setting to become available again.

## Optional Feature 9B: Maintenance Selector Switch (MSS)

Marked 'OFF', 'ON'.  This feature provides selector switch disconnection of control to the transfer motor thus allowing testing of the transfer switch control logic circuitry without initiating load transfer.  Manual disconnection is standard on all Eaton transfer switches.  Positioning the MSS in the 'OFF' position isolates the control circuit from the transfer motor, permitting manual operation of the transfer switch or testing of logic circuitry without load transfer.

## Optional Feature 10:  Preferred Source Selection (PRF SRC)

This feature permits the selection of either source (1 or 2) as the Preferred or Normal Source. The Normal Source is the source that the switch always looks to for availability so that it can transfer to it. When two generators are selected and the switch has transferred to the Emergency Source, the ATC-600 will constantly be waiting and attempting to start the generator on the Preferred Source so that it may return to it. IF NONE is chosen, the Preferred Source or the Normal Source will be the source that is presently attached to the load.

## Optional Feature 16:  Overcurrent Protection

When integral overcurrent protection is provided for either one or both sources, the need for separate upstream overcurrent protection, in most instances, is eliminated. With this factory installed feature in the ATC-600, further automatic transfer operation is locked-out until the appropriate source breaker is reset.

## Optional Feature 29G: Type of Operation (Selectable Automatic or Manual)

This feature provides a two position selector switch marked Auto/ Manual which permits the selection of automatic or manual operation.  It includes devices for manual operation when the selector switch is in the manual position.

## Optional Feature 29J:  Type of Operation (MANTR)

This feature provides for a selection between an automatic transfer and re-transfer mode or a manual pushbutton re-transfer to Normal from the Emergency Source mode. If this option is not selected the factory default selection is automatic.

<!-- PAGE 5 END -->

Effective: March 2010

## Optional Feature 32A:  Time Delay Neutral (TDN)

This feature provides a time delay in the transfer switch Neutral position when both breakers are open. This delay takes place when the load is transferred in either direction to prevent excessive in-rush currents due to out-of-phase switching of large motor loads. This feature is not available with the Neutral Load Sense Delay (TDNLD) feature.

## Optional Feature 32B:  Load Voltage Decay (LDCY)

This feature utilizes the load voltage measurements to sense back EMF that is generated when the transfer switch is in the Neutral position. It provides a delay in transfer in either direction if an unacceptable level is sensed as established by a customer programmed level. The transfer will not take place until the back EMF decays below the acceptable programmed level. This feature has a separate setting of enabling or disabling the operation. If disabled, the transfer switch will not delay in the Neutral position and will transfer between the sources as fast as possible. This feature is not available with the Time Delay Neutral (TDN) Feature 32A.

## Optional Feature 32C:  In-Phase/Load Voltage Decay

In-phase transition is a feature that will allow a transfer between two live sources only when the phase difference between the two sources is near zero.  This is an open transition transfer that prevents in-rush currents from exceeding normal starting currents in the case where motor loads are being transferred.

Load Voltage Decay utilizes the load voltage measurements to sense back EMF that is generated when the transfer switch is in the Neutral position.  It provides a delay in transfer in either direction if an unacceptable level is sensed as established by a customer programmed level.  The transfer will not take place until the back EMF decays below the acceptable programmed level.  This feature has a separate setting of enabling or disabling the operation.  If disabled, the transfer switch will not delay in the Neutral position and will transfer between the sources as fast as possible. This feature is not available with the Time Delay Neutral (TDN) Feature 32A.

## Optional Feature 32D:  In-Phase/Time Delay Neutral

In-phase transition is a feature that will allow a transfer between two live sources only when the phase difference between the two sources is near zero.  This is an open transition transfer that prevents in-rush currents from exceeding normal starting currents in the case  where motor loads are being transferred.

Time Delay Neutral provides a time delay in the transfer switch Neutral position when both breakers are open.  This delay takes place when the load is transferred in either direction to prevent excessive in-rush currents due to out-of-phase switching of large motor loads.  This feature is not available with the Neutral Load Sense Delay (TDNLD) feature.

## Optional Feature 35:  Pre-Transfer Signal (TPRE)

Typically associated with elevator controls, this feature provides for the control of an addressable relay to remotely signal an elevator that a re-transfer is about to take place. A permissive reportback signal from the elevator, telling the ATC-600 that the elevator has reached the floor and opened its doors, is also recognized to facilitate faster transfer operation. Should the permissive signal not be used or does not occur, the ATC-600 has a programmed overriding pre-transfer delay timer that can be set from 0 to 5 minutes.

For more information visit: www.eaton.com

<!-- image -->

## Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Optional Feature 36: Emergency Inhibit

This feature enables the Emergency Inhibit control input to inhibit transfers to the Emergency Source. See Control Inputs section for more information.

## Optional Feature 37:  Service Equipment

This factory programmed feature makes the transfer switch suitable for a service equipment rating by responding to a Go-To-Neutral input.

## Optional Feature 45:  Load Sequencing Capability (TSEQ)

This feature provides the sequential closure of up to 10 remote relays after a transfer. A customer programmed time delay is available to delay closure between each of the relays.

## Optional Feature 46:  Potential Transformer (PT) Ratio

This feature allows external voltage transformers to be used on the ATC-600's source and load sense inputs. Once this option is enabled, the PT Ratio setpoint can be adjusted in steps of 1, between 2:1 and 500:1. Also when this option is enabled the Nominal System Voltage setting will be fixed at 120 or 110 volts, depending upon the Nominal System Frequency setting. If the Nominal System Frequency setting is 60Hz then the Nominal System Voltage will be fixed at 120 volts and all voltage pick-up and drop-out setpoints will be based upon the 120 volt level. The same is true of a Nominal System Frequency of 50Hz whose Nominal System Voltage will be fixed at 110 volts. The metering display will use the PT ratio value to calculate and display the load and source voltages with up to three significant digits. There will be four possible types of displays, as an example they could display 999K, 99.9K, 9.99K, or 999 volts.

## 48: Communication Modules

Provides communications modules for the ATC-600 and ATC-800 transfer switch controllers. These controllers are PowerNet and Modbus compatible devices. A separately mounted communications module will enable the automatic transfer controller to be remotely monitored controlled and programmed via the network.

## 48F: RS-232 and RS-485 with Modbus

Provides communications for the ATC-600 via RS-232 or Modbus through an RS-485 port. Registers are available to read back status, voltages, frequencies, and historical data. Registers are also available for transfer switch control. Setpoints may be read back and/or programmed via a pass-through command.

<!-- PAGE 6 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Section 2:  Hardware Description

## 2.1  General

The purpose of this section is to familiarize the reader with ATC600 hardware, its nomenclature, and to list the unit's specifications. The information presented is divided into the following four parts:

- Operator Panel
- Rear Access Area
- External Hardware
- Specification Summary

## 2.2  Operator Panel

The operator panel, which is normally accessible from the outside of a panel or door, provides a means for:

- Being alerted to specific conditions
- Receiving functional help
- Programming
- Parameter Monitoring/Selection/Metering

LEDs, a display window, pushbuttons, and a mimic bus make up the front accessible operator panel (Figure 1 ).

Seventeen individual LEDs are lit when performing or indicating a specific function. For detailed information on individual LEDs refer to Paragraph 3.2.

The LED type display window is used to display all ATC-600 monitored parameters, setpoints and messages in easy to read formats. The alpha numeric display is approximately 0.75 by 4.25 inches and is able to display up to eight characters at a time. For details concerning the kind of information that can be viewed in the display window refer to Paragraph 3.3.

The front operator panel supports six long-life membrane pushbuttons. Pushbuttons accomplish their function when pressed and released. Refer to Paragraph 3.4 for information concerning the function of specific pushbuttons.

## 2.3  Rear Access Area

The rear access area of the ATC-600 is normally accessible from the rear of an open panel door (Figure 2 ).

All wiring connections to the ATC-600 are made at the rear of the chassis. For the sake of uniform identification, the frame of reference when discussing the rear access area is facing the back of the ATC-600 with the panel door open. The communication module port, for example, is located on the upper right rear of the unit. The Run/Program Switch, used to determine the ATC-600 Mode, is located in the lower right near the control power inputs. Detailed information relative to any connection made to the rear access area is presented in Section 4 entitled 'Operation.'

## 2.3.1  Left Rear of Chassis

The left rear of the chassis provides self locking female connectors J1, J2 and J3 for voltage monitoring of Source 1 (S1), Source 2 (S2) and the Load respectively. Terminal block J4 provides DC wetted connections for various functional inputs. See Paragraph 4.3 for more information on input functionality.

Effective: March 2010

Page 7

## 2.3.2  Right Rear of Chassis

The right rear of the chassis provides a port that will accept the D-sub male connector of the optional Communication Module (PONI). A self locking female connector J7 is provided for Sources 1 and 2 control power input.

Customer programming is provided through the Program/Run Toggle Switch. While the switch is in the Program position, the ATC-600 continues to operate in keeping with previously programmed setpoints.

Terminal block J5 provides dry relay contacts for primary control outputs. Physically these relays are comprised of two latching Form A relays for generator start contacts, and seven conventional coil Form C relays necessary to complete the electrical control function.

<!-- PAGE 7 END -->

Page 8

Effective: March 2010

<!-- image -->

1. ATC-600 Faceplate (UV Resistant)
2. Operational Mode LEDs (highlighting ATC-600's present operational condition)
3. System Status Mimic Bus (easy to read and understand LED type)
4. Display Window (easy to read monitored parameters, setpoints and messages)
5. Display LEDs (seven LEDs to identify the Display Window Information)
6. Help Pushbutton (provides English language help information in any operational mode)

Figure 1. ATC-600 Operator Panel.

7. Increase/Decrease Pushbuttons (used individually, pushbuttons move displayed information/setting up or down through all possibilities - used simultaneously while viewing historical logged values, values reset to zero)
8. Step Pushbutton (used to step through different available information within the category being displayed)
9. Display Select Pushbutton (used to move the display through the categories represented by the 7 LEDs under the display)
10. Engine Test Pushbutton (pushed and released twice to initiate a self test in Run or Program Modes

For more information visit: www.eaton.com

<!-- image -->

<!-- PAGE 8 END -->

<!-- image -->

Figure 2. ATC-600 (Left and Right Side Views).

<!-- image -->

## 2.4  External Hardware (Communication Module)

External hardware is viewed as any optional device mounted directly to or remotely from the ATC-600, such as a communication module. Communications is made possible by mounting a small, addressable communication module (PONI) to the back of the ATC-600 (Figure 3 ) or in a remote location. Since the ATC600 is always supplied with a communications port, a PONI can be easily retrofitted to the ATC-600 at any time. It is recommended that the control power to the ATC-600 be removed prior to connecting or disconnecting a PONI. When using the INCOM PONI on the ATC-600, the PONI function switches should be set to either of the Standard PONI modes (PONI 9600 Baud or PONI 1200 Baud). Refer to the instruction details supplied with the PONI for details.

Figure 3. Communication Module - PONI (mounted).

<!-- image -->

For more information visit: www.eaton.com

<!-- PAGE 9 END -->

Page 10

Effective: March 2010

## 2.5  Specification Summary

Refer to Table 1 .

## Table 1. ATC-600 Specifications

PARAMETER

| Control Power:                                              | • 120Vac (50/60 Hz) (operating range 65 to 160 Vac)                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power Consumption:                                          | • 18VA                                                                                                                                                                                                                                                                                                                                               |
| Environmental Conditions:                                   |                                                                                                                                                                                                                                                                                                                                                      |
| Operating Temperature                                       | • -20° to 70°C                                                                                                                                                                                                                                                                                                                                       |
| Operating Humidity                                          | • up to 90% Relative Humidity (non-condensing)                                                                                                                                                                                                                                                                                                       |
| Enclosure Compatibility:                                    | • NEMA 12 (standard mounting) • NEMA 4/4X (mounted with gasket between panel and device faceplate) • NEMA 3R (outdoor) • UV Resistant ATC-600 Faceplate                                                                                                                                                                                              |
| System Voltage Application:                                 | • 120 to 600 Vac (50/60 Hz) (single or three phase)                                                                                                                                                                                                                                                                                                  |
| Voltage Measurements:                                       | • Source 1, Source 2 and Load (VAB, VBC, VCA for Three Phase System)                                                                                                                                                                                                                                                                                 |
| Voltage Measurement Range:                                  | • 0 to 700 Vac                                                                                                                                                                                                                                                                                                                                       |
| Voltage Measurement Accuracy:                               | • ±1% of Full Scale                                                                                                                                                                                                                                                                                                                                  |
| Frequency Measurements:                                     | • Source 1 and Source 2                                                                                                                                                                                                                                                                                                                              |
| Frequency Measurement Range:                                | • 40 to 80 Hz                                                                                                                                                                                                                                                                                                                                        |
| Frequency Measurement Accuracy:                             | • ±0.1 Hz                                                                                                                                                                                                                                                                                                                                            |
| Undervoltage Dropout Range (Volts) Breaker Switch Style ATS | 50 to 97% of Nominal System Voltage                                                                                                                                                                                                                                                                                                                  |
| Undervoltage Pickup Range (Volts) Breaker Switch Style ATS  | (Dropout +2%) to 99% of Nominal System Voltage                                                                                                                                                                                                                                                                                                       |
| Overvoltage Dropout Range (Volts) Breaker Switch Style ATS  | 105 to 120% Nominal System Voltage                                                                                                                                                                                                                                                                                                                   |
| Overvoltage Pickup (Volts) Breaker Switch Style ATS         | 103% to (Dropout-2%) of Nominal System Voltage                                                                                                                                                                                                                                                                                                       |
| Underfrequency Dropout (Hertz) Breaker Switch Style ATS     | 90 to 97% of Nominal System Frequency                                                                                                                                                                                                                                                                                                                |
| Underfrequency Pickup (Hertz) Breaker Switch Style ATS      | (Dropout +1 Hz) to 99% of Nominal System Frequency                                                                                                                                                                                                                                                                                                   |
| Overfrequency Dropout (Hertz) Breaker Switch Style ATS      | 103 to 110% of Nominal System Frequency                                                                                                                                                                                                                                                                                                              |
| Overfrequency Pickup (Hertz) Breaker Switch Style ATS       | 101% to (Dropout -1 Hz) of Nominal System Frequency                                                                                                                                                                                                                                                                                                  |
| Applicable Testing:                                         | • UL Recognized Component • Meets Seismic Requirements of Uniform and California Building Codes (exceeding requirements of worst case Zone 4 levels) • Complies with UL 991 environmental tests • Complies with IEC 61000-4-2, 61000-4-3, 61000-4-4, and 61000-4-5 • Complies with CISPR 11, Class A • Complies with FCC Part 15, Subpart B, Class A |

SPECIFICATION

<!-- image -->

<!-- PAGE 10 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Section 3:  Operator Panel

## 3.1  General

The operator panel, which is normally accessible from the outside of a panel or door, provides a means for being alerted to specific conditions, receiving functional help, programming, and parameter monitoring/selection (Figure 1 ). For the purpose of familiarization, the panel is divided into three sub-sections and discussed individually:

- LEDs
- Pushbuttons
- Display Window

## NOTICE

WITH RESPECT TO THEIR USE IN THIS DOCUMENT AND AS THEY RELATE TO AUTOMATIC TRANSFER SWITCH OPERATION, THE WORDS 'CYCLE' AND 'EVENT' ARE DEFINED AS FOLLOWS:

CYCLE -A COMPLETE OPERATION FROM NORMAL TO EMERGENCY TO NORMAL.

EVENT -A FAILURE RESULTING IN SOME TYPE OF SWITCH AND/OR SWITCH INTELLIGENCE ACTION.

## NOTICE

REFER TO APPENDIX D FOR AN OVERALL VIEW OF ATC-600 OPERATIONS IN THE FORM OF A MENU TREE.

## 3.2  LEDS

LEDs are used to indicate the device's mode of operation, the status of the system, and the operations and/or conditions of displayed functions. Three LEDs at the top of the ATC-600 provide a quick snapshot of the unit's status (Mode). Seven LEDs, just above the display window, indicate which portions of the mimic bus are active, and the actual status of both sources and load. The remaining seven LEDs, just below the display window, are lit to indicate the identity of information being displayed.

## Automatic Mode LED

This LED blinks green indicating that the ATC-600 is operating and providing the transfer switch control function in keeping with programmed setpoints. If the LED is not lit or is on continuously, a problem may be indicated.

## Test Mode LED

This LED is lit red upon entering the Test Mode. The Test Mode can only be entered with the LEDs below the display window not lit. When a test is initiated, the Status LED lights. Both LEDs will turn off upon the successful completion of a test cycle.

## Program Mode LED

This LED is lit red when the Run/Program switch on the rear of the chassis is in the Program position. This condition permits programming of control setpoints. When the setpoints LED is lit indicating that existing setpoints can be changed, the Program Mode LED blinks.

## Source 1 Available - Status LED

This LED is lit amber if Source 1 meets the criteria for programmed Source 1 setpoints.

Effective: March 2010

Page 11

## Source 1 Preferred - Status LED

This LED is lit red if Source 1 is the preferred source choice.

## Source 1 Connected - Status LED

This LED is lit green if Source 1 is connected. This is accomplished by sensing the Source 1 breaker via the S1 closed auxiliary contact.

## Source 2 Available - Status LED

This LED is lit amber if Source 2 meets the criteria for programmed Source 2 setpoints.

## Source 2 Preferred - Status LED

This LED is lit red if Source 2 is the preferred source choice.

## Source 2 Connected - Status LED

This LED is lit red if Source 2 is connected. This is accomplished by sensing the Source 2 breaker via the S2 closed auxiliary contact.

## Load Energized - Status LED

This LED is lit red if the load is connected to a source that is available.

<!-- image -->

## CAUTION

LOAD ENERGIZE LED IS NOT A POSITIVE INDICATION THAT VOLTAGE IS NOT PRESENT ON THE LOAD TERMINALS.

## Status - Display LED

This LED is lit red when action is occurring, such as a timer timing down, and one of the other display categories has not been selected. When the action is completed, the display goes blank and the LED turns off. The Status position is the default position of the display.

## Source 1 - Display LED

This LED is lit green when displaying Source 1 voltage, frequency, and status information. The LED also lights when displaying specific Source 1 setpoint information.

## Source 2 - Display LED

This LED is lit red when displaying Source 2 voltage, frequency, and status information. The LED also lights when displaying specific Source 2 setpoint information.

## Load - Display LED

This LED is lit red when load voltage is being displayed.

## History - Display LED

This LED is lit red when displaying historical information.

## Time/Date - Display LED

This LED is lit red when displaying the time or date.

## Setpoints - Display LED

This LED is lit red when displaying the programmed setpoints of the ATC-600. When a specific displayed setpoint is associated with one of the sources, the specific source LED will also be lit.

<!-- PAGE 11 END -->

Effective: March 2010

Figure 4. Software and Options Identification Display.

Note: The entire Figure 4 message is shown for clarity, in actuality the message scrolls across the display as space permits.

## 3.3  Pushbuttons

The front operations panel supports six blue membrane pushbuttons. Pushbuttons accomplish their function when pressed and released. Certain pushbuttons, like the Increase and Decrease Pushbuttons, will also continue to scroll if they are pressed and not released. The Run/Program Switch, located on the right rear chassis, is not a membrane pushbutton. It will, however, be addressed in this section since it is required to move between the Run and Program Modes.

## 3.3.1  Run/Program Toggle Switch

The right rear mounted Run/Program Toggle Switch establishes whether the ATC-600 is in the Run Mode or the Program Mode. Normally the switch is set in the Run position to permit normal programmed operations. Programmed setpoints can only be altered with the switch in the Program position. Altered setpoints are stored and establish the new operating conditions of the ATC600 only after the switch is moved back to the Run position.

## 3.3.2  Help Pushbutton

When the Help Pushbutton is pressed and released with the ATC600 in any mode, an English language message will scroll across the display. Pushing and releasing the pushbutton a second time will abort the message. Messages and explanations relative to what is being viewed in the display are intended to prompt and assist the operator.

## NOTICE

PRESSING AND RELEASING THE HELP PUSHBUTTON WITH THE ATC-600 DISPLAY WINDOW BLANK CAUSES ALL OF THE FRONT PANEL LEDS TO MOMENTARILY LIGHT BEFORE SCROLLING A MESSAGE ACROSS THE DISPLAY (FIGURE 4). THE MESSAGE INDICATES THE SOFTWARE VERSION, REVISION NUMBER, AND AN ENCODED CATALOG NUMBER THAT REVEALS TO EATON WHAT SPECIFIC OPTIONS ARE INCLUDED WITH THIS PARTICULAR UNIT. THE CUSTOMER MAY BE ASKED FOR THIS INFORMATION BY EATON DURING A TROUBLESHOOTING OR RETURN PROCESS.

## 3.3.3  Engine Test Pushbutton

When the Engine Test Pushbutton is pressed and released twice with the ATC-600 in the status state, a self-test is initiated. This test can be initiated and accomplished while in the Run or Program Modes. Pressing the Engine Test Pushbutton again while in the engine run condition aborts the test.

Upon test initiation, a generator start of the non-preferred source is engaged after TDES timeout. If a full test is programmed, a transfer with all programmed timers occurs. The test engine run timer will hold the load for the required timeout and the test is concluded with a re-transfer cycle. For an engine run only test, no transfer will occur and the engine will run for the programmed run time.

## NOTICE

THE OPTIONAL PLANT EXERCISER FEATURE ALLOWS FOR AUTOMATIC PROGRAMMING OF THE DESIRED TEST CYCLE ON A WEEKLY BASIS. IF THE SWITCH IS UNABLE TO PROCESS EITHER A PLANT EXERCISER REQUEST OR THE ENGINE TEST PUSHBUTTON ITSELF DUE TO TRANSFER SWITCH STATUS, THE REQUEST IS IGNORED.

## 3.3.4  Display Select Pushbutton

As the Display Select Pushbutton is pressed and released, ATC600 steps through the following display categories:

- Status
- Source 1
- Source 2
- Load
- History
- Time
- Date
- Setpoints

## 3.3.5  Step Pushbutton

The Step Pushbutton steps through the different available information within the display category selected as the pushbutton is pressed and released.

When Source 1 is the category displayed for example, use of the Step Pushbutton will step the display through the voltages, frequency and status condition associated with Source 1. In the Time/Date category, however, this pushbutton has an additional purpose. The Step Pushbutton is also used to permit programming of the time and date by stepping through the different time and date categories (Hours, Minutes, Month, Day and Year). The actual time or date category is moved up or down using the Decrease or Increase Pushbuttons described next.

## 3.3.6  Increase and Decrease Pushbuttons

These pushbuttons, when pressed and released for step by step changes or held depressed for scrolling, increase or decrease setpoints while in the Programming Mode or make Time/Date changes. While historical information is being displayed, the Increase Pushbutton will scroll through events, and the Decrease Pushbutton will scroll through the actual time and date of the event. In addition, if both buttons are pressed and released simultaneously while viewing any of the historical logged values, the value resets to zero. Refer to paragraph 3.4.4 and Appendix B for additional information pertaining to accessing historical information and historical data definitions. Simultaneously pressing and releasing the Increase and Decrease Pushbuttons will also reset an alarm condition.

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

<!-- PAGE 12 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## 3.4  Display Window

The ATC-600 provides a comprehensive array of monitored parameters, setpoints and messages via its easy to read Display Window. Up to eight large characters are used to convey a wealth of information. Eight different displays can be presented via the Display Window:

- Status Display
- Source 1 Display
- Source 2 Display
- Load Display
- History Display
- Time/Date Display
- Setpoints Display
- Help Display

## NOTICE

ALTHOUGH A WIDE VARIETY OF PARAMETERS AND SETPOINTS CAN BE DISPLAYED, THEY ARE NOT DISPLAYED IF THEY WERE NOT ORIGINALLY ORDERED AND PROGRAMMED.

## NOTICE

WHETHER VIEWING OR PROGRAMMING, THE ALPHA-NUMERIC DISPLAY IS BLANKED IF NO PUSHBUTTON ACTIVITY IS DETECTED FOR APPROXIMATELY 2 1/2 MINUTES.

## 3.4.1  Status Display

This display provides messages regarding anything that is presently changing or happening to the switches status, including source information, timer countdowns and failure reports. The display functions in a similar manner, whether in the Automatic, Test or Program Modes (Figure 5 ). Refer to Appendix A for a complete list of Status Display messages.

<!-- image -->

Figure 5. Typical Time Delay Normal to Emergency Time Display Upon Normal Source Loss.

Figure 6. Typical Source 1 Display (Single Phase Line Voltage RMS - Source1).

<!-- image -->

Figure 7. Typical History Display (Source 2 Engine Run Time in Hours).

<!-- image -->

Effective: March 2010

Figure 8. Typical Setpoints Display (Time Delay Engine Start Minutes and Seconds).

<!-- image -->

## 3.4.2  Source 1 and 2 Displays

These displays indicate the present status of the sources in terms of voltage, frequency and condition (Figure 6 ). If the source is available the condition display will be 'GOOD,' if it is unavailable one of the following possible conditions will be shown.

- OVER-V

The source has risen above the dropout setting and not dropped below the pickup setting.

- UNDER-V

The source has dropped below the dropout setting and not risen above the pickup setting.

- OVER-F

The source has risen above the dropout setting and not dropped below the pickup setting.

- UNDER-F

The source has dropped below the dropout setting and not risen above the pickup setting.

## 3.4.3  Load Display

This display indicates the voltage and frequency of the connected load.

## 3.4.4  History Display

This display indicates historical and cumulative values as follows (Figure 7 ):

- Source 1 Engine Run Time
- Source 2 Engine Run Time
- Source 1 Connected Time
- Source 2 Connected Time
- Total Availability Time Source 1
- Total Availability Time Source 2
- Total Time Load Energized
- Total Number of Transfers
- Time/Date/Reason for 16 most recent transfers

## NOTICE

REFER TO PARAGRAPH 3.3.6 (INCREASE AND DECREASE PUSHBUTTONS) AND APPENDIX B FOR ADDITIONAL INFORMATION PERTAINING TO ACCESSING HISTORICAL INFORMATION AND HISTORICAL DATA DEFINITIONS.

## 3.4.5  Time/Date Display

This display indicates real-time in terms of hours, minutes and seconds on one display and month, day and year on a second display. It also indicates individual time items for programming purposes.

## NOTICE

REFER TO PARAGRAPHS 3.3.4 (DISPLAY SELECT PUSHBUTTON), 3.3.5 (STEP PUSHBUTTON), 3.3.6 (INCREASE AND DECREASE PUSHBUTTONS) AND APPENDIX C FOR ADDITIONAL INFORMATION PERTAINING TO TIME/DATE INFORMATION.

<!-- PAGE 13 END -->

Page 14

Effective: March 2010

## 3.4.6  Setpoints Display

This display indicates presently programmed setpoints. The setpoints can only be altered in the Program Mode. Keep it mind, if a feature was not originally ordered and programmed, it will not be displayed (Figure 8 ). Refer to Section 5 for details.

## 3.4.7  Help Display

This display presents moving English language messages, explanations and prompts to assist the operator while in any of the three operational modes. When the Help Pushbutton is pressed and released a second time during the scrolling of a message, the message is aborted.

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Section 4:  Operation

## 4.1  General

This section specifically describes the operation and functional use of the ATC-600. It is divided into three main categories:

- Automatic Mode
- Test Mode
- Programming Mode

The practical use of and operation within each specific category will be discussed. In this section it is assumed that prior sections were reviewed and that the operator has a basic understanding of the hardware. It is important that the operator have a good grasp of the functional use of the operator panel as covered in Section 3. This will make movement within each category and between categories a simple task. This familiarity will quickly put the unsurpassed capabilities of ATC-600 at the operator's fingertips.

## NOTICE

IT IS IMPORTANT TO REMEMBER THAT ATC-600 CONTINUES TO PROVIDE PROGRAMMED PROTECTION AND AUTOMATIC OPERATION NO MATTER WHICH MODE THE DEVICE IS IN AT THE TIME IT IS CALLED UPON TO OPERATE.

## NOTICE

REFER TO APPENDIX D FOR AN OVERALL VIEW OF ATC-600 OPERATIONS IN THE FORM OF A MENU TREE.

## 4.2 Automatic Mode

The Automatic Mode of ATC-600 provides for automatic transfer and re-transfer from source to source as dictated by the features supplied and their programmed setpoint values. It provides a summary of ATC-600's intelligence and supervisory circuits which constantly monitor the condition of both normal and emergency power sources thus providing the required intelligence for transfer operations. These circuits, for example, automatically initiate an immediate transfer of power when power fails or voltage levels drop below a preset value. Exactly what ATC-600 will initiate in response to a given system condition depends upon the combination of standard and selected optional features. Refer to Paragraphs 1.3 and 1.4 for ATC-600's standard and optional features.

When the preferred source is connected and the automatic transfer switch is operating normally, the Automatic LED blinks green and no message appears in the display window. In the event of a power failure, the display automatically becomes active showing the status of timers relative to an alternate source transfer. Once the alternate source becomes available, the transfer is made consistent with pre-programmed features. In a similar manner, transfer back to the preferred source is made once the preferred source is again available. System conditions relative to the sources and the load are clearly indicated by the LED type mimic bus.

## 4.3  Control Inputs

As described in Section 2, the rear access area provides for access to all input connections. Each control input provides 50 volts at 10ma. Refer to Figure 3 for a graphical representation and position of all input connections.

<!-- PAGE 14 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## NOTICE

## CERTAIN INPUTS MAY NOT BE OPERATIONAL DEPENDING ON USER PURCHASED OPTIONS.

ATC-600 provides for eight individual control input signals on terminal block J4. as follows:

## Source 1 Auxiliary Close

This input is located on Pins 1 and 2 of Connector J4 and wired to the Source 1 breaker auxiliary contact that is closed when the Source 1 breaker is closed.

## Source 2 Auxiliary Close

This input is located on Pins 3 and 4 of Connector J4 and wired to the Source 2 breaker auxiliary contact that is closed when the Source 2 breaker is closed.

## Lockout

This input is located on Pins 5 and 6 of Connector J4. The contact is closed to indicate that both the Source 1 and Source 2 breakers are available. Opening of this contact signifies a tripped circuit breaker or circuit breaker non-availability which will cause ATC-600 to inhibit further operation.

## Go To Emergency

This input is located on Pins 7 and 8 of Connector J4. When the external contact is closed, a transfer to the Emergency Source will be initiated. If the Emergency Source should fail and the Normal Source is available, the ATC-600 will initiate a transfer back to the Normal Source.

The Go To Emergency input is only active when either Source 1 or Source 2 is preferred. This input is not active when the Preferred Source selection is set to None.

The Emergency Inhibit input takes priority over the Go To Emergency input if both inputs are activated at the same time. In this case, the generator will start but a transfer to the Emergency Source will be inhibited until the Emergency Inhibit input is deactivated.

## Bypass Timers

A momentary closure on Pins 9 and 10 of Connector J4 will bypass the timer for TDNE and/or TDEN.

## Go To Neutral

A maintained closed contact on Pins 11 and 12 of Connector J4 forces the controller to switch to the neutral position, thereby disconnecting the load from both sources.

## Manual Re-Transfer

With manual operation set, momentary closure on Pins 13 and 14 of Connector J4 allows ATC-600 to proceed with a re-transfer operation at the operators discretion. Should a failure of the emergency source occur while waiting for the manual return, the retransfer proceeds automatically.

## Emergency Inhibit

This input is located on Pins 15 and 16 of Connector J4 and is enabled when the Emergency Inhibit optional feature (36) is enabled. The contact is closed for normal operation. Opening this contact will activate the Emergency Inhibit input.

If the Emergency Inhibit contact is opened when the load is connected to the Normal Source, no action will be taken if the Normal Source is available. If the Normal Source is not available, an immediate transfer to the neutral position will occur.

Effective: March 2010

Page 15

If the Emergency Inhibit contact is opened when the load is connected to the Emergency Source, the ATC-600 will transfer the load to the Normal Source if it is available. If the Normal Source is not available, an immediate transfer to the neutral position will occur.

The Emergency Inhibit input is only active when either Source 1 or Source 2 is preferred. This input is not active when the Preferred Source selection is set to None.

The Emergency Inhibit input takes priority over the Go To Emergency input if both inputs are activated at the same time. In this case, the generator will start but a transfer to the Emergency Source will be inhibited until the Emergency Inhibit input is deactivated.

## INCOM Sub-Network

Pins 17, 18 and 19 of Connector J4 provide for the INCOM (Industrial Communications) interface. Refer to Communications Mode in this section for more information.

## 4.4  INCOM Sub-Network

Pins 17, 18 and 19 of connector J4 provide for the INCOM (Industrial Communications) sub-network interface. From the ATC-600 a single twisted pair of wires can remotely communicate with devices up to 7500 feet away. Using the same technology and protocol as our IMPACC communications network this system will allow the ATC-600 to be a master to Addressable Relay IIs that accomplish the Pre-transfer and Load Sequencing features. The sub-network can be enabled for either or both of these features. The Addressable Relay IIs are a product that is part of the IMPACC family of communicating products. The addressable Relay II is a form C relay that includes 2 status inputs, a LED to show the status of the relay and a LED to show the communications transmit status. Figure 9 shows a typical configuration that has both the Pre-transfer and Load Sequencing features enabled.

## 4.4.1  Pre-transfer Sub-Network

The Pre-transfer signal as previously described allows for loads, typically an elevator, to communicate with the ATC-600. The important design features of this configuration are that the relay can be located up to a mile away and it reports back its status and the state of input IN1.

The Addressable Relay II must be set for:

- 1200 BAUD rate
- WATCHDOG feature disabled
- RELAY PULSE feature disabled
- Address set for 001
- Reportback input IN1

## NOTICE

IF POWER IS LOST TO THE ADDRESSABLE RELAY II IT WILL POWERUP IN THE DE-ENERGIZED (OPEN) STATE.

<!-- PAGE 15 END -->

Page 16

Effective: March 2010

Figure 9. Typical Wiring of Addressable Relays to the ATC-600.

<!-- image -->

The IN1 connections of the relay are the reportback input to the ATC-600 and should be connected to a contact output from the elevator controller. Refer to the Addressable Relay II and the elevator controller manufacturer's instruction literature for proper control power and input signal voltage levels. When proper operating voltage is present between the IN1 input pins, a positive status will be reported back to the ATC-600. During normal operation the relay's contact will be de-energized. When a transfer is pending and after the TDNE (or TDEN) timer has counted down (if enabled), the ATC-600 will send a communications close command to the relay. Once the relay has closed, the ATC-600 will start the Time Delay Pre-transfer count down timer to delay the transfer operation until the counter has finished. After the timer has started, the ATC-600 will continuously poll the relay for the status of its input circuit. If the relay returns a positive status of IN1, the ATC-600 will assume that the elevator has arrived at the proper floor and opened the doors. The ATC-600 will then abort the remaining Time Delay Pre-transfer timer and continue with the transfer operation. Once the transfer is complete, the ATC-600 will return to the relay and send a communication open command. This option is only functional if closed and In-phase modes are disabled.  The Pre-transfer sequence only occurs if both sources are available.  If only one source is available, the Pre-transfer

## 4.4.2  Load Sequencing Sub-Network

The Load Sequencing signal allows loads to be activated in a sequence after a transfer has taken place. Addressable Relay II's are used to enable up to 10 separate loads.

The Addressable Relay II must be set for:

- 1200 BAUD rate
- WATCHDOG feature disabled
- RELAY PULSE feature disabled
- Address range from 002 to 00B

Under normal condition with source available, Addressable Relay AR II (connected to ATC-600 Controller at J4-17, J4-18, J4-19) is energized. For breaker type transfer switch, before the switch has moved from neutral position to the new source, all 10 of the sequence relays are sent open commands. For contactor type transfer switch (2-position or 3-position), as soon as the time delay normal to emergency (or time delay emergency to normal) times out, all 10 of the sequence relays are sent open commands. The ATC-600 will make several attempts to communicate with a relay.  If an address or relay is not used or if a relay fails to respond, the ATC-600 will move on to the next relay. Once the attempt to turn all the relays off has been made, the ATC-600 will start to sequence the 10 relays on. Starting with address 002, the ATC-600 will send the relay the command to close. After this relay responds, the ATC-600 will start the Time Delay Sequence timer (TSEQ). When this timer has counted down to zero, the ATC-600 will increment to the next address of 003 and send it the close command. Should there be no relay, the ATC-600 will display the NO R xx (where xx is the address) message on the front panel, abort the time delay and then step to the next address. This will continue until a relay that responds is reached or after address 00B, which is the last address, is tested.

For more information visit: www.eaton.com

sequence is bypassed.

<!-- image -->

<!-- PAGE 16 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## 4.4.3 ATC Annunciator

The ATC Annunciator provides remote annunciation of an ATC600 which may be located up to 1000 feet away. The ATC Annunciator will communicate with the ATC-600 over the INCOM Subnetwork using a twisted shielded pair cable. Required power is either 120 VAC 50/60Hz or 24 VDC.

The ATC Annunciator displays the ATC-600 information through six LEDs as described below:

## Source 1 Available

This white LED is lit if Source 1 meets the criteria for programmed Source 1 setpoints.

## Source 1 Connected

This green LED is lit when the Source 1 breaker is closed.

## Source 2 Available

This amber LED is lit if Source 2 meets the criteria for programmed Source 2 setpoints.

## Source 2 Connected

This red LED is lit when the Source 2 breaker is closed.

## Comm OK

This green LED is lit when the ATC Annunciator is communicating properly with the ATC-600.

## In Test

This red LED indicates that the ATC-600 is in Test mode.

## 4.5  Relay Outputs

As described in Section 2, the rear access area provides for access to all output connections. Refer to Figure 3 for a graphical representation and position of all output connections. The relay functions are divided into two categories:

- Customer Connections
- Transfer Operation Contacts

## 4.5.1  Customer Connections

## S2 Generator

This latched coil relay provides a Form A contact on Pins 1 and 2 of Connector J5. The relay is the generator start relay for system configurations employing a generator on the input source designated Source 2. The generator start relay contacts are rated for 5A, 1/6 HP @ 250 VAC. The DC rating is 5A @ 30VDC with a 150W maximum load.

## S1 Generator

This latched coil relay provides a Form A contact on Pins 3 and 4 of Connector J5. The relay is the generator start relay for system configurations employing a generator on the input source designated Source 1. The generator start relay contacts are rated for 5A, 1/6 HP @ 250 VAC. The DC rating is 5A @ 30VDC with a 150W maximum load.

## Alarm

This Form C relay is used to indicate an alarm condition. The full Form C contact of this relay is implemented with Common Pin 8, Normally Closed Pin 7, and Normally Open Pin 6 of Connector J5. The relay is normally de-energized to indicate the absence of an alarm state. Energization of the relay indicates the presence of an alarm condition. Alarm conditions include improper circuit breaker operation, motor operator failure, and unsuccessful closed or inphase transition. An alarm may be reset by simultaneously pressing the Increase and Decrease Pushbuttons.  The relay contacts are rated for 10A, 1-3 HP @ 250 VAC. The DC rating is 10A @30VDC.

## S2 Available

This Form C relay is used to indicate the availability of Source 2. The full Form C contact of this relay is implemented with Common Pin 11, Normally Closed Pin 10, and Normally Open Pin 9 of Connector J5. This relay essentially duplicates the Source 2 available status LED meaning that the setpoint criteria has been met. The relay contacts are rated for 10A, 1-3 HP @ 250 VAC. The DC rating is 10A @30VDC.

## S1 Available

This Form C relay is used to indicate the availability of Source 1. The full Form C contact of this relay is implemented with Common Pin 14, Normally Closed Pin 13, and Normally Open Pin 12 of Connector J5. This relay essentially duplicates the Source 1 available status LED meaning that the setpoint criteria has been met. The relay contacts are rated for 10A, 1-3 HP @ 250 VAC. The DC rating is 10A @30VDC.

## 4.5.2 Transfer Operation Connections

K1, K2, K3, and K4 are factory wired to operate the transfer switch. The relay contacts for each are rated for 10A, 1/3 HP @ 250 VAC. The DC rating is 10A @30VDC. K1- K4 are Form C relays but only the Form A contacts are used to operate the transfer switch.

Note: The ATC-600 Controller MUST BE properly grounded at J-5, Pin 5 for proper operation.

## Output Relay K1

The K1 output is used for control of the transfer switch motor to close the Source 1 switching device (i.e. circuit breaker) for motor-operator transfer switches. The K1 relay momentarily energizes until the ATC-600 senses that the Source 1 switching device is closed, then K1 de-energizes. For transfer switches with power breakers, this relay opens the Source 2 breaker via its trip coil. The k1 output is found on pins 21 and 22 of Connector J5

## Output Relay K2

The K2 output is used for control of the transfer switch motor to close the Source 2 switching device (i.e. circuit breaker) for motor-operator transfer switches. The K2 relay momentarily energizes until the ATC-600 senses that the Source 2 switching device is closed, then K2 de-energizes. For transfer switches with power breakers, this relay opens the Source 1 breaker via its trip coil. The K2 output is found on pins 19 and 20 of Connector J5.

## Output Relay K3

The K3 output is used for control of the close coil of the Source 1 breaker in transfer switches with power breakers. The K3 relay momentarily energizes until the ATC-600 senses that the Source 1 breaker is closed, then K3 de-energizes. The K3 output is found on pins 17 and 18 of Connector J5.

Effective: March 2010

<!-- PAGE 17 END -->

Page 18

Effective: March 2010

## Output Relay K4

The K4 output is used for control of the close coil of the Source 2 breaker in transfer switches with power breakers. The K4 relay momentarily energizes until the ATC-600 senses that the Source 2 breaker is closed, then K4 de-energizes. The K4 output is found on pins 15 and 16 of Connector J5.

## 4.6  Test Mode

The Test Mode is intended to permit the periodic performance of tests of the system. To enter the Test Mode, the display window must be blank.

When the Engine Test Pushbutton is pressed and released, 'START' will be shown in the display window and the Status LED will be lit. At this point, if the initiation of a test is not desired, pressing the Increase and Decrease Pushbuttons simultaneously will clear the display window. In addition, if any of the display pushbuttons are not touched for 2 1/2 minutes, the Test Mode and Display Window would be cleared. If a test is desired, the Engine Test Pushbutton must be pressed a second time before the 2 1/2 minutes have expired. At this time the Status and Test Mode LEDs are lit red, and one Test Mode cycle is implemented.

The exact test conditions are determined by programmed setpoints. Whether or not to transfer the load during testing, disable the engine test completely, and the engine test run time are operator selected parameters. Refer to Section 5 Programming and specifically Table 2 for test programming details.

A load transfer test cycle includes a full generator start, a transfer, and a re-transfer. For the test cycle to proceed, the Normal Source must be available. The test cycle will be aborted if the Emergency Source does not become available within a set time-out period, or if a needed source becomes unavailable. In addition, the test will be aborted if the Test Pushbutton is again pressed and released. Both LEDs turn off upon the successful completion of a test cycle, once the time delay engine cool down timer has expired and the generator is stopped.

If the 'Number of Generators' setpoint is programmed to zero, the Engine Test Pushbutton is not functional. If the setpoint is programmed to two, the test will be performed on the generator not connected to the load.

When an engine test is in progress, it may be aborted the following ways:

1. By pressing the 'Engine Test' pushbuttton.
2. If the Emergency Source does not become available within 90 seconds of the ATC-600 providing the engine start command.
3. If , during the TDNE countdown, the Emergency Source goes unavailable more than three times. (Each time, TDNE will restart.)
4. If the Emergency Source is powering the load and it goes unavailable for more than the TDEF setting.
5. If the Normal source becomes unavailable.

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## 4.7  Programming Mode

ATC-600 is fully programmable from the device's faceplate once the Run/Program switch on the rear of the chassis has been moved to the Program position. Any operator associated with programming the ATC-600 will quickly discover that ATC-600 programming is just a matter of simple, repetitive steps. Because of the importance placed, however, on this function and its critical relationship to the systems proper functioning, Section 5 is dedicated to the Programming Mode. Refer to this section and Table 2 for details.

## 4.8  Communications

ATC-600 is an IMPACC (Integrated Monitoring Protection and Control Communications) compatible device. As such, it can be remotely monitored, controlled and programmed when equipped with the communications option. The ATC-600 is supplied with a communications port as standard. This permits it to have the communications option supplied from the factory or retrofitted at a later date. The communications option is achieved by mounting a small, addressable communications module, the PONI, to the back of the ATC-600 (Paragraph 2.4 and Figure 3 ).

IMPACC is a noise immune communications system that permits communications from the ATC-600 to a master computer via a high frequency carrier signal over a shielded twisted pair of conductors. The shielded twisted pair of conductors can extend up to 7500 feet without the use of repeaters. Communications between IMPACC compatible devices, such as ATC-600 and the master computer is made possible by the INCOM (Industrial Communications) chip, which accounts for the system's high degree of reliability.

## 4.8.1  IMPACC Powernet Software

PowerNet software provides the ability to monitor and record power distribution system data as it is occurring. PowerNet is a Microsoft Windows compatible application featuring user friendly, menu-driven screens with easy set-up and operation. Additional features include:

- System/device alarm logging and reporting
- Time/event historical data logging
- Data trending
- Information storage/retrieval by device event
- Hardware diagnostics
- Dedicated computer not required
- Security password protection
- Gateway interface for connectivity to other information networks

IMPACC PowerNet also provides the following features unique to the ATC-600:

- Duplication of ATC-600 front panel mimic bus showing available and connected sources.
- Voltage and frequency measurements of Source 1 and Source 2. Voltage measurements of the Load.
- Display of all programmed setpoint values. These values may be changed and either saved to a file or downloaded to the ATC600 over IMPACC.

<!-- PAGE 18 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## NOTICE

IF THE ATC-600 RUN/PROGRAM SWITCH IS IN THE PROGRAM POSITION, THE SETPOINTS CANNOT BE DOWNLOADED OVER IMPACC.

- History information:

Source 1 Engine Run Time

Source 2 Engine Run Time

Source 1 Available Time

Source 2 Available Time

Source 1 Connected Time

Source 2 Connected Time

Load Energized Time

Number of Transfers

All history information is in hours and minutes. Each individual value is resettable over IMPACC.

- Time-stamped history (time/date/reason) for all previous transfers.
- Capability to initiate an engine test.
- Updates the ATC-600 real-time clock.

## 4.9  In-phase Transition

In-phase transition is an open transition with both sources inphase.  The same anticipatory scheme used for closed transition is also used for in-phase transition.  The advance angle is calculated based on the frequency difference between the two sources and also the response time of the breaker.  This results in the optimum reconnect angle of 0 degrees for all of the frequency difference values.

The criteria for in-phase transition are similar to closed transition. Both sources must be available and the frequency difference must be less than the in-phase transition frequency difference setpoint (0.0 to 3.0 Hz).  When these conditions are met, the ATC-600 will monitor the phase difference between the two sources.  The synchronization timer will count down and be displayed as 'TSIP' while waiting for synchronization to be detected.  When the phase difference is within the advance angle window, the 'transfer' command is given.  This is an open transition but both sources will be in phase when the transfer occurs.

If the synchronization does not occur within a specified amount of time, the transfer will take place under delayed transition.The Alarm relay will energize and the failure will be logged into the Transfer History as either 'Sync Fail - Freq' or 'Sync Fail - Phase' depending on whether the frequency difference or the phase difference was excessive.

Effective: March 2010

## Section 5:  Programming

## 5.1  Introduction

## NOTICE

ALTHOUGH ALL ATC-600 PROGRAMMABLE FEATURES ARE ADDRESSED IN THIS SECTION, ONLY THOSE ORDERED BY THE CUSTOMER AND INITIALLY PROGRAMMED AT THE FACTORY WILL APPEAR IN THE DISPLAY FOR PROGRAMMING CHANGES IN THE FIELD.

The ATC-600 is fully programmable from the device's faceplate or through the communications port. Users can reprogram setpoints as well as other parameters. The time and date can be changed while the device is in either the Run Mode or the Program Mode. Setpoints, however, can only be changed while the device is in the Program Mode.

## 5.2  Entering and Exiting the Program Mode

## NOTICE

WHILE IN THE PROGRAM MODE, ATC-600 IS NEVER OFF-LINE AND CONTINUES TO FUNCTION IN ACCORDANCE WITH PREVIOUSLY PROGRAMMED SETPOINTS.

## NOTICE

IF NO PUSHBUTTON ACTIVITY IS DETECTED FOR APPROXIMATELY 2 1/2 MINUTES WHILE IN THE PROGRAM MODE, THE SETPOINTS LED IS CLEARED AND THE ALPHA-NUMERIC DISPLAY IS BLANKED. ANY PREVIOUSLY MADE SETPOINT CHANGES ARE NOT SAVED, SHOULD THIS OCCUR.

## NOTICE

WHEN THE TOGGLE SWITCH IS IN THE PROGRAM POSITION, REMOTE COMMUNICATIONS PROGRAMMING IS INHIBITED.

To enter the Program Mode, move the Run/Program Toggle Switch located on the right rear chassis to the Program position. Once the Program Mode is activated, the Program LED blinks red and continues until the Program Mode is exited.

When programming changes have been completed, the Program Mode is exited by moving the Run/Program Toggle Switch back to the Run position. At that point, the Automatic LED continues to blink green, the alphanumeric display shows the word 'Program' for a short period, and the Program LED will no longer be illuminated. It is also at that point when any setpoint changes are saved in the device's non-volatile memory.

## 5.3  Programming Procedures

Once the Program Mode has been entered, use the Display Select Pushbutton to move to the Setpoints Display. The Setpoints LED will be lit red and the first programming possibility will appear in the display. Use the Step Pushbutton to move from one feature setpoint to another, stopping at those in need of reprogramming. Use the Increase or Decrease Pushbuttons to move the display to a new setpoint selection. Once a new setpoint selection has been made, move to the next feature in need of change. Once all setpoints are displayed as required, exit the Program Mode and the new setpoints are automatically stored.

<!-- PAGE 19 END -->

Page 20

Effective: March 2010

## 5.4  Programmable Features/Setpoints

<!-- image -->

## CAUTION

CHANGING THE SYSTEM NOMINAL VOLTAGE OR FREQUENCY SETPOINTS WILL AUTOMATICALLY CHANGE ALL THE PICKUP AND DROPOUT SETTINGS TO NEW DEFAULT VALUES.

## Table 2. Programmable Features/Setpoints.

| PROGRAMMABLE    | DISPLAY                                                                       | SETPOINT                                                        | FACTORY DEFAULT   | FACTORY DEFAULT    |
|-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------|-------------------|--------------------|
| FEATURE DISPLAY | EXPLANATION                                                                   | RANGE                                                           | VALUE             | MEASURE            |
| TDES            | Time Delay Engine Start Timer                                                 | 0 to 120 Seconds                                                | 0:03              | Minutes: Seconds   |
| TDNE            | Time Delay Normal to Emergency Timer                                          | 0 to 1800 Seconds                                               | 0:00              | Minutes: Seconds   |
| TDEN            | Time Delay Emergency to Normal Timer                                          | 0 to 1800 Seconds                                               | 5:00              | Minutes: Seconds   |
| TDEC            | Time Delay Engine Cool Down Timer                                             | 0 to 1800 Seconds                                               | 5:00              | Minutes: Seconds   |
| NOMF            | System Nominal Frequency (Hertz)                                              | 50 or 60 Hz 3                                                   | 60                | Hertz              |
| NOMV            | System Nominal Voltage (Volts)                                                | 120 to 600 Volts 3                                              | 120               | Volts              |
| 1UVD            | Source 1 Undervoltage Dropout (Volts)                                         | 97 to 50% of Nominal 1                                          | 80%               | Volts              |
| 2UVD            | Source 2 Undervoltage Dropout (Volts)                                         | 97 to 50% of Nominal 1                                          | 80%               | Volts              |
| 1UVP            | Source 1 Undervoltage Pickup (Volts)                                          | (Dropout +2%) to 99% 1                                          | 90%               | Volts              |
| 2UVP            | Source 2 Undervoltage Pickup (Volts)                                          | (Dropout +2%) to 99% 1                                          | 90%               | Volts              |
| 1OVD            | Source 1 Overvoltage Dropout (Volts)                                          | 105 to 120% 1                                                   | 115%              | Volts              |
| 2OVD            | Source 2 Overvoltage Dropout (Volts)                                          | 105 to 120% 1                                                   | 115%              | Volts              |
| 1OVP            | Source 1 Overvoltage Pickup (Volts)                                           | 103% to (Dropout-2%) 1                                          | 110%              | Volts              |
| 2OVP            | Source 2 Overvoltage Pickup (Volts)                                           | 103% to (Dropout-2%) 1                                          | 110%              | Volts              |
| 1UFD            | Source 1 Underfrequency Dropout (Hertz)                                       | 90 to 97% 2                                                     | 94%               | Hertz              |
| 2UFD            | Source 2 Underfrequency Dropout (Hertz)                                       | 90 to 97% 2                                                     | 94%               | Hertz              |
| 1UFP            | Source 1 Underfrequency Pickup (Hertz)                                        | (Dropout +1 Hz) to 99% 2 2                                      | 96%               | Hertz              |
| 2UFP            | Source 2 Underfrequency Pickup (Hertz)                                        | (Dropout +1 Hz) to 99%                                          | 96%               | Hertz              |
| 1OFD 2OFD       | Source 1 Overfrequency Dropout (Hertz) Source 2 Overfrequency Dropout (Hertz) | 103 to 110% 2 103 to 110% 2                                     | 106% 106%         | Hertz Hertz        |
| 1OFP            | Source 1 Overfrequency Pickup (Hertz)                                         | 101% to (Dropout -1 Hz) 2                                       | 104%              | Hertz              |
| 2OFP            | Source 2 Overfrequency Pickup (Hertz)                                         | 101% to (Dropout -1 Hz) 2                                       | 104%              | Hertz              |
| TDN TDNLD       | Time Delay Neutral Timer Time Delay Neutral Load Decay                        | 0 to 120 Seconds 0 =Disabled                                    | 0:00 1            | Minutes: Seconds - |
| LDCY            | Load Decay Voltage                                                            | 1 =Enabled 2 to 30% of Nominal Voltage                          | 30                | Volts              |
| PRF SRC         | Preferred Source                                                              | None 1=Source 1                                                 | 1                 | -                  |
| EXER            | Plant Exerciser Enabled or Disabled                                           | 2=Source 2 1=Enabled 0= Disabled                                | 1                 | -                  |
| EXLD            | Load Transfer with Plant Exerciser                                            | 1=Enabled 0= Disabled                                           | 1                 | -                  |
| PEDAY           | Plant Exerciser Day of Week                                                   | 1 to 7                                                          | 1                 | Week Day           |
|                 |                                                                               | (1= Sunday)                                                     |                   |                    |
| PEH             | Plant Exerciser Hour                                                          | 1 am to 11 pm                                                   | 1 AM              | Hour               |
| PREMIN          | Plant Exerciser Minute                                                        | 0 to 59 Minutes                                                 | 0                 | Minutes            |
| CTDNE           | Commitment to Transfer in TDNE                                                | 1= PB Return 0= Not Committed                                   | 0                 | -                  |
|                 |                                                                               | 1= Committed                                                    | 1                 | -                  |
| TMODE           | Engine Test With/Without Load Transfer                                        | 0= No Load Transfer 1= Load Transfer 2= Disable Test Pushbutton |                   | Hours: Minutes     |
| TER             | Engine Test/Plant Exerciser Run Time                                          | 0 to 600 Minutes                                                | 0:30              | Minutes: Seconds   |
| TPRE            | Pre-Transfer Sub-Network Time Delay                                           | 1 to 300 Seconds                                                | 0:01              |                    |
| GENNO           | Number of Generators (Single Generator Must Be On Source 2)                   | 0 to 2                                                          | 1                 | -                  |

For more information visit: www.eaton.com

<!-- image -->

All ATC-600 programmable features and associated setpoint possibilities with any required explanations are presented in Table 2 . Remember, only features originally ordered and factory programmed will appear in the display.

<!-- PAGE 20 END -->

<!-- image -->

Table 2. Programmable Features/Setpoints (Cont.)

| PROGRAMMABLE FEATURE DISPLAY   | DISPLAY EXPLANATION                              | SETPOINT POSSIBILITIES   | FACTORY DEFAULT   | FACTORY DEFAULT   |
|--------------------------------|--------------------------------------------------|--------------------------|-------------------|-------------------|
|                                |                                                  |                          | VALUE             | MEASURE           |
| PHASE                          | Number of System Phases                          | 1 or 3 3                 | 3                 | -                 |
| TSEQ                           | Time Delay Load Sequencing                       | 1 to 120 Seconds         | 0:10              | Minutes: Seconds  |
| PT                             | PT Ratio                                         | 2:1 to 500:1             | 2:1               | -                 |
| IPHASE                         | In-Phase Transition Enabled or Disabled          | 1= Enabled 0= Disabled   | 0                 | -                 |
| IPFD                           | In-Phase Transition Frequency Difference (Hertz) | 0.0 to 3.0 Hz            | 1.0               | Hertz             |
| SYNC                           | Closed/In-Phase Transition Synchronization Timer | 1 to 60 Minutes          | 5                 | Minutes           |
| TDEF                           | Time Delay Engine Failure                        | 0 to 60 Seconds          | 6                 | Seconds           |

Note 1: Voltage pickup and drop out settings are based upon a percentage of the base voltage

Note 2: Frequency pickup and drop out settings are based upon a percentage of the base frequency

Note 3: Set to order specific value

Effective: March 2010

Page 21

<!-- PAGE 21 END -->

Page 22

Effective: March 2010

## Section 6:  Troubleshooting and Maintenance

## 6.1  Level of Repair

This manual is written with the assumption that only transfer switch system troubleshooting will be performed. If the cause of malfunction is traced to an ATC-600, the unit should be replaced with a spare. The malfunctioning unit should then be returned to Eaton for factory repairs.

## Table 3. Troubleshooting Guide.

| SYMPTOM                                                                                                                         | PROBABLE CAUSE                                                                                                                                                                          | POSSIBLE SOLUTION(S)                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All front panel indicator LED's are off.                                                                                        | Control power is deficient or absent. ATC-600 is malfunctioning.                                                                                                                        | Verify that control power is connected at J7 and that it is within specifications. Replace the unit.                                                                                                                                 |
| Automatic LED is not blinking.                                                                                                  | Control power is deficient or absent. Stuck waiting for Neutral position ATC-600 is malfunctioning                                                                                      | Verify that control power is connected at J7 and that it is within specifications. Mechanical problem; No reportback from limit switch. Replace the unit.                                                                            |
| One or more voltage phases read incorrectly.                                                                                    | Incorrect wiring. ATC-600 is malfunctioning.                                                                                                                                            | Verify voltage with multimeter. Check wiring. Replace the unit.                                                                                                                                                                      |
| Front panel pushbuttons do not work.                                                                                            | Bad connection inside ATC-600.                                                                                                                                                          | Replace the unit.                                                                                                                                                                                                                    |
| Unit did not accept new setpoints via front panel.                                                                              | Operator error. No pushbuttons pressed for 2.5 minutes.                                                                                                                                 | Change setpoints with switch in Program position. Return switch to Run position to save setpoints before pressing Display Selectpushbutton. Avoid intervals of 2.5 minutes of inactivity with pushbuttons when changing set- points. |
| Voltage dropout and pickup setpoints are different than what was programmed.                                                    | Adjusted nominal voltage setpoint.                                                                                                                                                      | Re-adjust all dropout and pickup setpoints to default values.                                                                                                                                                                        |
| Frequency dropout and pickup setpoints are differ- ent than what was programmed.                                                | Adjusted nominal frequency setpoints.                                                                                                                                                   | Re-adjust all dropout and pickup setpoints to default values.                                                                                                                                                                        |
| Changed undervoltage or overvoltage or underfre- quency or overfrequency dropout setpoint and the pickup setpoint changed also. | Pickup upper or lower limit ranges are dependent upon dropout setpoints. To prevent misapplication, they are automatically adjusted when overlapping occurs.                            |                                                                                                                                                                                                                                      |
| Source 1 or Source 2 is not available when it should be.                                                                        | Voltage and/or frequency is not within setpoint values.                                                                                                                                 | Verify voltage and/or frequency with multi-meter. Check programmed setpoint values.                                                                                                                                                  |
| Source 1 or Source 2 is not shown connected when it should be on faceplate LEDs.                                                | Do not have contact closure at S1 or S2 AUX CLOSE control input. ATC-600 is malfunctioning.                                                                                             | Verify contact closure at desired control input on J4. Replace the unit.                                                                                                                                                             |
| Engine fails to start after TDES times out.                                                                                     | S1 or S2 Generator start relay contacts not closed. Incorrect wiring at generator.                                                                                                      | Replace the unit. Check engine wiring/maintenance.                                                                                                                                                                                   |
| Engine fails to turn off after TDEC times out.                                                                                  | S1 or S2 Generator start relay contacts not open. Incorrect wiring at generator. Connected LED not lit for either source.                                                               | Replace the unit. Check engine wiring. Verify contact closure at desired control input on J4. Replace the unit.                                                                                                                      |
| Unit will not perform an Engine Test.                                                                                           | Engine Test pushbutton was not pressed twice. Display window is not blank before initiating test.                                                                                       | Press Engine Test pushbutton twice to initiate test. Use Display Select pushbutton to toggle to Status LED. If a timer is timing down, wait until it is done.                                                                        |
| Unit displays 'WAIT 0.00'                                                                                                       | Voltage and/or frequency of generator is not within setpoint values.                                                                                                                    | Verify voltage and/or frequency with multi-meter. Check programmed setpoint values.                                                                                                                                                  |
| Plant exerciser (PE) failed to exercise.                                                                                        | Incorrect date or time setting. Incorrect setpoint programmed for PE day and/or time. Generator voltage and/or frequency did not become available within 30 seconds of engine starting. | Verify real time settings for Time/Date. Re-program PE day and/or time setpoint. Verify voltage and/or frequency with multi-meter. Check programmed setpoint val- ues. Check engine maintenance.                                     |
| Unit displays Lock-Out.                                                                                                         | Circuit breaker tripped. Maintenance Selector Switch in disable position. Lock-out circuit wiring problem.                                                                              | Check for overload/short circuit condition. Check Maintenance Selector Switch. Check lock-out circuit wiring.                                                                                                                        |
| Unit displays 'INHIBIT'                                                                                                         | No contact closure at Emergency Inhibit Input                                                                                                                                           | Check Emergency Inhibit Wiring at J4, Pins 15 and 16                                                                                                                                                                                 |

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## NOTICE

DURING CONVERSATIONS WITH EATON CONCERNING TROUBLESHOOTING OR PRODUCT RETURN, THE CUSTOMER MAY BE ASKED FOR INFORMATION PERTAINING TO THE SOFTWARE VERSION AND OPTIONS INCLUDED IN THE SPECIFIC UNIT. REFER TO THE 'NOTE' UNDER THE TOPIC 'HELP PUSHBUTTON' IN PARAGRAPH 3.4 FOR INSTRUCTIONS ON HOW TO OBTAIN THIS INFORMATION.

## 6.2  ATC-600 Device Troubleshooting

The Troubleshooting Guide (Table 3 ) is intended for service personnel to identify whether a problem being observed is

<!-- PAGE 22 END -->

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

Table 3. Troubleshooting Guide (Cont.)

| SYMPTOM                                                     | PROBABLE CAUSE                                                                                      | POSSIBLE SOLUTION(S)                                                                                                                       |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Unit displays 'S1 BRKR'                                     | Source 1 circuit breaker did not open when it was com- manded to open.                              | Check Source 1 circuit breaker shunt trip (ST) wiring. Press Increase and Decrease push-buttons simultaneously to clear message.           |
| Unit displays 'S1 BRKR'                                     | Source 1 circuit breaker did not close when it was com- manded to close.                            | Check Source 1 circuit breaker spring release (SR) wiring. Press Increase and Decrease push-buttons simultaneously to clear message.       |
| Unit displays 'S1 BRKR'                                     | S1 Aux Close contacts did not open when Source 1 breaker opened.                                    | Check S1 Aux Close control input wiring on J4-1,2. Press Increase and Decrease push-buttons simultaneously to clear message.               |
| Unit displays 'S1 BRKR'                                     | S1 Aux Close contacts did not close when Source 1 breaker closed                                    | Check S1 Aux Close control input wiring on J4-1,2. Press Increase and Decrease push-buttons simultaneously to clear message.               |
| Unit displays 'S2 BRKR'                                     | Source 2 circuit breaker did not open when it was com- manded to open.                              | Check Source 2 circuit breaker shunt trip (ST) wiring. Press Increase and Decrease push-buttons simultaneously to clear message.           |
| Unit displays 'S2 BRKR'                                     | Source 2 circuit breaker did not close when it was com- manded to close.                            | Check Source 2 circuit breaker spring release (SR) wiring. Press Increase and Decrease push-buttons simultaneously to clear message.       |
| Unit displays 'S2 BRKR'                                     | S2 Aux Close contacts did not open when Source 2 breaker opened.                                    | Check S2 Aux Close control input wiring on J4-1,2. Press Increase and Decrease push-buttons simultaneously to clear message.               |
| Unit displays 'S2 BRKR'                                     | S2 Aux Close contacts did not close when Source 2 breaker closed                                    | Check S2 Aux Close control input wiring on J4-3,4. Press Increase and Decrease push-buttons simultaneously to clear message.               |
| Unit fails to communicate over Load Sequencing- subnetwork. | Addressable Relay(s) set to incorrect address.                                                      | Set Addressable Relay(s) address from 002 to 00B.                                                                                          |
| Unit fails to communicate over Load Sequencing- subnetwork. | Addressable Relay(s) set to incorrect baud rate. Addressable Relay(s) Watchdog and Relay Pulse fea- | Set Addressable Relay(s) baud rate to 1200 baud (SW1 =ON). Disable Addressable Relay(s) Watchdog and Relay Pulse features (SW2, SW3 =OFF). |
| Unit fails to communicate over Load Sequencing- subnetwork. | Incorrect Addressable Relay(s) reportback input used.                                               | Wire to IN1 reportback input of Addressable Relay(s).                                                                                      |
| Unit fails to communicate over Load Sequencing- subnetwork. | Twisted pair wiring not used between Addressable Relay(s) and ATC-600.                              | Use Belden 9463 twisted pair, Eaton IMPCABLE, or equivalent.                                                                               |
| Unit fails to communicate over Load Sequencing- subnetwork. | Addressable Relay(s) control power deficient or absent.                                             | Verify Addressable Relay(s) control power of 96 to 144 VAC or 48 to 125 VDC.                                                               |
| Unit fails to communicate over IMPACC network.              | Wrong or conflicting address set on PONI.                                                           | Check that PONI has a unique address on the system and that software is addressing proper unit.                                            |
| Unit fails to communicate over IMPACC network.              | Communications wiring errors.                                                                       | Verify wiring is in conformance to IMPACC wiring rules. Replace PONI.                                                                      |
| Unit fails to communicate over IMPACC network.              | PONI failure.                                                                                       |                                                                                                                                            |
| Unit fails to communicate over IMPACC network.              | ATC-600 is malfunctioning.                                                                          | Replace the unit.                                                                                                                          |
| Unit did not allow setpoints to be downloaded over IMPACC.  | Run/Program switch is not in Run position.                                                          | Set Run/Program switch to Run position.                                                                                                    |
| Unit did not allow setpoints to be downloaded over IMPACC.  | IMPACC communications error.                                                                        | See 'Unit fails to communicate over IMPACC network.'                                                                                       |

external or internal to the unit. For assistance with this determination, contact Eaton. If a problem is identified to be internal, the unit should be returned to the factory for repair or replacement.  If a problem is identified to be external to ATC-600, proceed to Section 6.3 and continue troubleshooting.

## NOTICE

WHILE PERFORMING TESTING, IF AN UNDESIRED OR UNDOCUMENTED RESULT OCCURS, FIRST CONTACT THE LOCAL GENSET DEALER. IF THE RESULT IS NOT CORRECTED, CONTACT THE EATON POWER QUALITY TECHNICAL SUPPORT CENTER AT 1-800-354-2070

Effective: March 2010

Page 23

<!-- PAGE 23 END -->

Page 24

Effective: March 2010

## 6.3 Problem Solving

<!-- image -->

## WARNING

HAZARDOUS VOLTAGES IN AND AROUND TRANSFER SWITCH EQUIPMENT DURING THE PROBLEM SOLVING PROCESS CAN CAUSE PERSONAL INJURY AND/OR DEATH. AVOID CONTACT WITH ANY VOLTAGE SOURCE WHILE PROBLEM SOLVING.

<!-- image -->

## WARNING

ONLY PROPERLY TRAINED PERSONNEL FAMILIAR WITH THE TRANSFER SWITCH EQUIPMENT AND ITS ASSOCIATED EQUIPMENT SHOULD BE PERMITTED TO PERFORM THE PROBLEM SOLVING FUNCTION.  IF AN INDIVIDUAL DOES NOT FEEL QUALIFIED TO PERFORM THE PROBLEM SOLVING FUNCTION, THE INDIVIDUAL SHOULD NOT ATTEMPT TO PERFORM ANY OF THESE PROCEDURES.

This section explains basic troubleshooting for Magnum Breaker Transfer Switches. A basic problem solving effort is the first step to take prior to calling for assistance.  Frequently, the effort will successfully address most problems encountered.  The problem solving procedure is presented in the following paragraphs as observed Problem Symptoms and one or more possible Solution Steps.  All of the steps presented may not apply to all transfer switches, depending upon the logic.  Remember, only qualified individuals familiar with the transfer switch equipment and the system in which it is applied should attempt these problem solving procedures.

If a problem persists after having completed the problem solving procedure, contact an Eaton representative for further assistance. When calling for assistance, the following is the minimum information required to properly address the need:

1. Shop Order Number (SO#) or General Order Number (GO#) of transfer switch, plus related Item Number
2. Catalog and/or Style Number of transfer switch
3. Actual location of transfer switch (type of facility, address, etc.)
4. Company name
5. Name and position of individual representing company
6. Basic description of situation as it exists
7. Any results of problem solving steps taken and/or readings taken

<!-- image -->

## Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## 6.3.1  Transfer switch appears inoperative

- Step 1: Verify that all plugs and sockets are properly interconnected.
- Step 2: Verify that the correct system voltage appears at NORMAL switch.  Measure the voltage at the breaker lugs.
- Step 3: Verify that the voltage selection plug is in the proper position to match the system voltage.
- Step 4: Look for any obviously burned components.  Determine the cause and rectify, if possible.  Replace defective components after the cause is determined.
- Step 5: Press the push-to-close button on the normal switching device.  Verify whether or not the system voltage now appears on the load terminals.
- If YES: Proceed to check logic for problems in respective logic instruction book.
- If NO:  Check all power connections and the switching mechanism.

## 6.3.2   Transfer Switch Will Not Automatically Transfer To Normal

Step 1: Is Option 29 installed?  If so, there would be a pushbutton labeled 'Manual Transfer to Normal.'

- If YES:STOP!  The transfer switch must be MANUALLY transferred to NORMAL by depressing the pushbutton.
- If NO:  Proceed to Step 2.
- Step 2: Is Option 9B installed?  If so, there would be a selector switch labeled 'Maintenance.'
- If YES:  Verify selector switch is in the 'Operate' position.
- If NO:   Proceed to Step 3.
- Step 3: Are the correct line voltage and frequency available at terminals N1, N2 and N3?  Record the readings.
- If YES: Proceed to Step 4.
- If NO:  Check NORMAL source
- Step 4: Is the voltage selector plug in the correct position?
- If YES:  Proceed to Step 5.

If NO:

Position plug correctly.

- Step 5: Check the voltage on transformer NT1 by measuring voltage between voting relay KV-1 and GND.  Is the voltage measured 120 Vac (+/- 10 volts)?  Record the reading.

If YES:  Proceed to Step 6.

- If NO:   Check voltage transformer NT1.

For more information visit: www.eaton.com

<!-- PAGE 24 END -->

<!-- image -->

## Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

- Step 6: Is the NORMAL switching device charged?

If YES:Proceed to Step 7.

If NO: Go through paragraph 6.3.4 first before continuing.

- Step 7: Is the NORMAL power source available?

If YES:Proceed to Step 8.

If NO: Apply the correct system voltage to NORMAL connections.

- Step 8: Is the EMERGENCY switch OPEN?

If YES:Proceed to Step 10.

If NO: Proceed to Step 9.

- Step 9: Measure the voltage between terminals B10 and B11 on the EMERGENCY switching device (shunt trip). Is the voltage measured 120 Vac (+/- 10 volts)?  Record the reading.

If YES: Refer to the magnum breaker maintenance manual IB#2C12060 and check the shunt trip EMERGENCY switch.

If NO: Check the wiring to B10 and B11.

- Step 10: Measure the voltage between terminals B12 and B13 on the NORMAL switching device (spring release coil). Is the voltage measured 120 Vac (+/- 10 volts)?  Record the reading.

If YES: Refer to the magnum breaker maintenance manual IB#2C12060 and check the spring release coil NORMAL switching device.

If NO: Check the wiring to B12 and B13.

Step 11: If a problem persists, contact Eaton.

## 6.3.3  Transfer Switch Will Not Automatically Transfer To Emergency

Step 1:

If the alternate source is a generator, is it running?

If YES: Proceed to Step 2.

If NO: Check the generator.  Check the engine start contacts.

- Step 2: Are the correct line voltage and frequency available at terminals E1, E2 and E3?  Record the readings.

If YES: Proceed to Step 3.

If NO: Verify that there is output voltage from the generator.

Effective: March 2010

Page 25

Step 3: Is the voltage selector plug in the correct position?

If YES:  Proceed to Step 4.

If NO:   Position plug correctly.

Step 4: Is the NORMAL source available?

If YES: Proceed to Step 5.

If NO:  Proceed to Step 6.

Step 5: Is a test (Manual or Exercise) being run?

If YES: STOP!  The transfer switch should not transfer to EMERGENCY.  The NORMAL source is preferred.

If NO:  Proceed to Step 6.

- Step 6: Check the voltage on transformer ET1 by measuring voltage between voting relay KV-8 and GND.  Is the volt- age measured 120 Vac (+/- 10 volts)?  Record the read- ing.

If YES: Proceed to Step 7.

If NO:  Check voltage transformer ET1.

- Step 7: Is the EMERGENCY switching device charged?

If YES: Proceed to Step 8.

If NO:  Go through paragraph 6.3.4 first before continuing.

Step 8: Is the NORMAL switching device OPEN?

If YES: Proceed to Step 10.

If NO:  Proceed to Step 9.

Step 9: Measure the voltage between terminals B10 and B11 on the NORMAL switching device (shunt trip). Is the volt- age measured 120 Vac (+/- 10 volts)?  Record the read- ing.

If YES: Refer to the magnum breaker maintenance manual IB#2C12060 and check the shunt trip

NORMAL switch.

If NO: Check the wiring to B10 and B11.

- Step 10: Measure the voltage between terminals B12 and B13 on the EMERGENCY switching device (spring release coil). Is the voltage measured 120 Vac (+/- 10 volts)? Record the reading.

If YES: Refer to the magnum breaker maintenance manual IB#2C12060 and check the spring release coil EMERGENCY switching device.

If NO:

Check the wiring to B12 and B13.

Step 11: If a problem persists, contact Eaton.

<!-- PAGE 25 END -->

Page 26

Effective: March 2010

## 6.3.4  Transfer Switch Will Not Automatically Recharge Switches

- Step 1: Measure the voltage between terminals B15 and B14 on the switching device that does not automatically recharge. Is the voltage measured 120 Vac (+/- 10 volts)?  Record the reading.

If YES:Refer to the magnum breaker maintenance manual IB#2C12060 and check the electrical operator inside the switching device.

If NO: Verify the wiring to B15 and B14.

Step 2: If a problem persists, contact Eaton.

## 6.4  Replacement

Follow these procedural steps to replace the ATC-600.

- Step 1: Turn off control power at the main disconnect or isolation switch of the control power supply. If the switch is not located in view from the ATC-600, lock it out to guard against other personnel accidentally turning it on.
- Step 2: Verify that all 'foreign' power sources wired to the ATC600 are de-energized. These may also be present on some of the terminal blocks.
- Step 3: Before disconnecting any wires from the unit, make sure they are individually identified to assure that reconnection can be correctly performed. Make a sketch to help with the task of terminal and wire identification.
- Step 4: Remove all wires and disconnect plug-type connectors.

## NOTICE

SUPPORT THE ATC-600 FROM THE FRONT SIDE WHEN THE SCREWS ARE LOOSENED OR REMOVED IN STEP 5. WITHOUT SUCH SUPPORT, THE UNIT COULD FALL OR THE PANEL COULD BE DAMAGED.

- Step 5: Remove the 6 mounting screws holding the unit against the door or panel. These are accessed from the rear of the unit.
- Step 6: Carefully lay the screws aside for later use.
- Step 7: Mount the replacement unit.
- Step 8: Reverse the procedure outlined in Steps 4 and 5.
- Step 9: Using the sketch mentioned in Step 3, replace each wire at the correct terminal, and make sure each is secure. Make certain that each plug is securely seated

Step 10: Restore control power.

## 6.5  Maintenance and Care

The ATC-600 is designed to be a self contained and maintenance free unit. The printed circuit boards are calibrated and conformally coated at the factory. They are intended for service by factory trained personnel only.

For more information visit: www.eaton.com

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

<!-- PAGE 26 END -->

<!-- image -->

## Appendix A:  Status Display Messages

All possible Status Display Messages are shown below. For additional information, refer to paragraph 3.4.1.

Status Display Message

Display Message Meaning

TDEC

Countdown cool off timing before generator contacts are opened.

TDES

Countdown timing before generator contacts are closed.

TDNE

Countdown timing before normal breaker is opened for transfer to the emergency source.

TDN

Countdown timing with both sources disconnected from the load.

TXFR

Waiting for the switch to make the transfer from neutral position to the intended source.

TDEN

Countdown timing before the emergency breaker is opened for transfer to the normal source.

NEUTRAL

Both breakers are opened and the load is disconnected.

MANUAL

Waiting for an input signal to complete the manual re-transfer.

LOCK-OUT

A trip condition has been detected by either breaker and the system is locked-out from further transfers, or Option 9B, Maintenance Selector Switch, is in the 'OFF' position.

TER

The engine run test timer is counting down before the test is completed. Pressing the Engine Test pushbutton will abort this timer and the test.

START

To initiate an engine test sequence press Engine Test pushbutton again or press Increase and Decrease simultaneously to clear.

WAIT

Waiting for the generator source voltage and frequency to become available.

TDNV

Waiting for load voltage to decay before completing the transfer.

TDP

Countdown timing while waiting for a pre-transfer acknowledge input.

TSEQ

Countdown timing between sequenced loads.

NO R xx

No communications response on the sub-network was received from Addressable Relay II, set for address xx.

WAIT NEU

Waiting for the neutral position to be reached by the switch.

WAIT S1

Waiting for Source 1 breaker to open/close during a WLI closed transition.

WAIT S2

Waiting for Source 2 breaker to open/close during a WLI closed transition.

TSIP

Countdown timing while waiting for sources to synchronize for an in-phase transition.

S1 BRKR

Indicates that the Source 1 circuit breaker failed to open or close.

S2 BRKR

Indicates that the Source 2 circuit breaker failed to open or close.

TDEF 1

Countdown timing before declaring Source 1 unavailable. This is only implemented if the load is connected to Source 1 and Source 1 is a generator.

TDEF 2

Countdown timing before declaring Source 2 unavailable. This is only implemented if the load is connected to Source 2 and Source 2 is a generator.

ABORT

Indicates that an engine test or plant exercise was aborted after three unsuccessful attempts. The Emergency Source did not remain available while TDNE was timing.

INHIBIT

Indicates that a transfer to the Emergency Source is inhibited because the Emergency Inhibit input is activated.

For more information visit: www.eaton.com

Effective: March 2010

Page 27

<!-- PAGE 27 END -->

Page 28

Effective: March 2010

## Appendix B: Historical Display Information

This display indicates historical and cumulative values. The following information offers all possible historical displays, their definitions and accessing/reset instructions.

## Source 1 Engine Run Time

When two generators have been selected and programmed, this time will be shown as one of the parameters in the History display. This counter logs generator #1's run time in hours. Time will start being logged at the time the S1 GENERATOR contacts are closed, and it will stop as soon as they are opened. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Source 2 Engine Run Time

When one or two generators have been selected and programmed, this time will be shown as one of the parameters in the History display. This counter logs generator #2's run time in hours. Time will start being logged at the time the S2 GENERATOR contacts are closed, and it will stop as soon as they are opened. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Source 1 Connected Time

This counter logs time in hours whenever Source 1 is connected to the load. Time will start being logged at the time the S1 AUX control input is closed. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Source 2 Connected Time

This counter logs time in hours whenever Source 2 is connected to the load. Time will start being logged at the time the S2 AUX control input is closed. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Availability Time Source 1

When Source 1 meets the voltage and frequency setpoint criteria, this counter logs the time in hours. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Availability Time Source 2

When Source 2 meets the voltage and frequency setpoint criteria, this counter logs the time in hours. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Total Time Load Energized

When either of the two sources are connected to the load and the connected source is available, this counter will start logging the time in hours. This counter will count up to 9999 hours and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

## Total Number of Transfers

This counter logs the number of transfer cycles that occur. This counter will count up to 9999 cycles and then turn over. When viewing this value it can be reset to zero by pressing the Increase and Decrease pushbuttons at the same time.

For more information visit: www.eaton.com

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

## Time/Date/Reason for 16 Most Recent Events

The 16 most recent transfer events are stored in history and may be viewed at the front panel display as follows:

- Use the Display Select Pushbutton to display the History category
- Use the Step Pushbutton to step to the 'TFR HIST' display message
- Press and release the Increase Pushbutton to display the most recent transfer event, 'T01,' along with the type and cause of the event as exampled on next page:

<!-- PAGE 28 END -->

<!-- image -->

<!-- image -->

Effective: March 2010

Page 29

## Transfer Event Display Example

<!-- image -->

## Value Description

- 1 Open transition or Delayed from Source 1 to Source2
- 2 Open transition or Delayed from Source 2 to Source 1
- 3 In-phase transition from Source 1 to Source 2
- 4 In-phase transition from Source 2 to Source 1
- 5 Closed transition from Source 1 to Source 2
- 6 Closed transition from Source 2 to Source 1
- Pressing the Decrease Pushbutton will then display the date of the event.
- Pressing the Decrease Pushbutton again will display the time of the event.
- Continually pressing the Decrease Pushbutton will cycle the display between the event display, the date of the event and the time of the event.
- Pressing the Increase Pushbutton will display the next most recent transfer event, 'T02.' After the 16th event, 'T16,' is displayed, 'TFR HIST' is the next display shown. Continually pressing the Increase Pushbutton will start displaying the transfer events starting with 'T01' again.
- Pressing the Display Select Pushbutton, while viewing any of the transfer history displays, will step the display to the Time/Date display.

<!-- image -->

## Value Description

- 1 Preferred source became available
- 2 Overvoltage on connected source1
- 3 Undervoltage on connected source
- 4 Overfrequency on connected source
- 5 Underfrequency on connected source
- 6 Exercised generator
- 7 Engine test
- 8 Manual re-transfer
- 9 Engine Test via communications
- 10 Go to neutral
- 11 Program mode
- 12 Options or setpoints error
- 13 Emergency Inhibit
- 14 Go to Emergency
- 15 Lock-out
- 16 Failed to synchronize (Phase angle difference)
- 17 Failed to synchronize (Frequency difference)
- 18 Failed to synchronized (voltage difference)
- 19 Aborted test

<!-- PAGE 29 END -->

Page 30

Effective: March 2010

## Appendix C:  Time/Date Display Information

This display indicates real-time and date information. Pressing the Display Select Pushbutton the first time will display the present Time information. Pressing the Display Select Pushbutton again will display the present Date information. It is not required that the ATC-600 be in the Program Mode to change any of the Time or Date information.

## NOTICE

THE REAL TIME CLOCK CORRECTS FOR LEAP YEAR BUT NOT DAYLIGHT-SAVING TIME.

## TIME

In the Time Display, the present hours, minutes and seconds are shown. By using the Step Pushbutton, the hours, minutes and day of the week can be individually viewed. When individually viewed, these values can be adjusted.

- Hours

By using the Increase or Decrease Pushbuttons, the hours of the day can be adjusted to the present value. The number will continuously roll over between AM and PM values.

- Minutes

By using the Increase or Decrease Pushbuttons, the minutes of the day can be adjusted to the present value. The number will continuously roll over between 0 and 59 values.

- Day

By using the Increase or Decrease Pushbuttons, the day of the week can be adjusted between 1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday,   7 = Saturday.

## DATE

In the Date Display, the present month, day, and year are shown. By using the Step Pushbutton, the month, day and year can be individually viewed. When individually viewed these values can be adjusted.

- Month

By using the Increase or Decrease Pushbuttons, the month can be adjusted to the present value. The number will continuously roll over between 1 (January) and 12 (December) values.

- Day

By using the Increase or Decrease Pushbuttons, the day of the month can be adjusted to the present value. The number will continuously roll over between 0 and 31 values.

- Year

By using the Increase or Decrease Pushbuttons, the year can be adjusted to the present value. The number will continuously roll over between 00 and 99 values.

<!-- image -->

Instructions for Installation, Operation and Maintenance of the Eaton ATC-600 Automatic Transfer Switch Controller

<!-- PAGE 30 END -->

<!-- image -->

## Appendix D:  ATC-600 Menu Tree

<!-- image -->

## with In-PhaseTransition

For 1 Phase Sensing with In-PhaseTransition

<!-- image -->

Note: All menu items are not necessarily shown on every unit due to programmed settings or purchased options.

Note: Display Select, Step and Decrease, as used on this menu tree, represent the use of that specific Operator Panel Pushbutton.

Effective: March 2010

Page 31

<!-- PAGE 31 END -->

Page 32

Effective: March 2010

<!-- image -->

<!-- image -->

<!-- PAGE 32 END -->

<!-- image -->

## Appendix E: Operational Flowcharts

- Utility - Generator Transfer Switch
- Dual Utility Transfer Switch
- In-phase Transition Implementation

## Utility - Generator Transfer Switch

<!-- image -->

Effective: March 2010

Page 33

<!-- PAGE 33 END -->

## Dual Utility Transfer Switch

<!-- image -->

<!-- image -->

<!-- PAGE 34 END -->

<!-- image -->

## In-phase Transition Implementation

<!-- image -->

<!-- PAGE 35 END -->

## Instructional Booklet

Page 36

Effective: March 2010

This instruction booklet is published solely for information purposes and should not be considered all-inclusive.  If further information is required, you should consult an authorized Eaton sales representative.

The sale of the product shown in this literature is subject to the terms and conditions outlined in appropriate Eaton selling policies or other contractual agreement between the parties.  This literature is not intended to and does not enlarge or add to any such contract.  The sole source governing the rights and remedies of any purchaser of this equipment is the contract between the purchaser and Eaton.

NO WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE OR MERCHANTABILITY, OR WARRANTIES ARISING FROM COURSE OF DEALING OR USAGE OF TRADE, ARE MADE REGARDING THE INFORMATION, RECOMMENDATIONS, AND DESCRIPTIONS CONTAINED HEREIN.  In no event will Eaton be responsible to the purchaser or user in contract, in tort (including negligence), strict liability or otherwise for any special, indirect, incidental or consequential damage or loss whatsoever, including but not limited to damage or loss of use of equipment, plant or power system, cost of capital, loss of power, additional expenses in the use of existing power facilities, or claims against the purchaser or user by its customers resulting from the use of the information, recommendations and description contained herein.

CSA is a registered trademark of the Canadian Standards Association. National Electrical Code and NEC are registered trademarks of the National Fire Protection Association, Quincy, Mass. NEMA is the registered trademark and service mark of the National Electrical Manufacturers Association.  Uniform Building Code (UBC) is a trademark of the International Conference of Building Officials (ICBO). UL is a federally registered trademark of the Underwriters Laboratories Inc.

Eaton Corporation Electrical Group 1000 Cherrington Parkway Moon Township, PA 15108 United States 877-ETN CARE (877-386-2273) Eaton.com

© 2010 Eaton Corporation All Rights Reserved Printed in USA Publication No. IBATS-1005/TBG00220 March 2010

<!-- image -->

<!-- PAGE 36 END -->

