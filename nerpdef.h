// nerpdef.h
//
// Lego RR NERPS function call macros
//
// Copyright (C) 2009-2010 Johan Grip
// 
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
//


//
// Objectives and tutorial
//
#define _SetTutorialFlags(x) SetTutorialFlags x
#define _GetObjectiveSwitch() GetObjectiveSwitch
#define _GetObjectiveShowing() GetObjectiveShowing
#define _SetLevelCompleted() SetLevelCompleted

//
// Monsters
//
#define _GetSlugsOnLevel() GetSlugsOnLevel
#define _GenerateSlug() GenerateSlug

//
// Data gathering
//
#define _GetCrystalsCurrentlyStored() GetCrystalsCurrentlyStored
#define _GetToolStoresBuilt() GetToolStoresBuilt
#define _GetMiniFiguresOnLevel() GetMiniFiguresOnLevel
#define _GetOxygenLevel() GetOxygenLevel
#define _GetUnitAtBlock(x) GetUnitAtBlock x
#define _GetRecordObjectAtTutorial(x) GetRecordObjectAtTutorial x
#define _GetTutorialBlockIsGround(x) GetTutorialBlockIsGround x
#define _GetRandom100() GetRandom100

//
// On-screen message handling
//
#define _SetMessagePermit(x) SetMessagePermit x
#define _SetMessage(x,y) SetMessage x y
#define _GetMessageTimer(x) GetMessageTimer x
#define _SetMessageTimerValues(x,y,z) SetMessageTimerValues x y z


//
// Camera functions
//
#define _SetCameraGotoTutorial(x) SetCameraGotoTutorial x
#define _CameraUnlock() CameraUnlock


//
// Register manipulations
//
#define _SetR0(x) SetR0 x
#define _SetR1(x) SetR1 x
#define _SetR2(x) SetR2 x
#define _SetR3(x) SetR3 x
#define _SetR4(x) SetR4 x
#define _SetR5(x) SetR5 x
#define _SetR6(x) SetR6 x
#define _SetR7(x) SetR7 x

#define _GetR0(x) GetR0 x
#define _GetR1(x) GetR1 x
#define _GetR2(x) GetR2 x
#define _GetR3(x) GetR3 x
#define _GetR4(x) GetR4 x
#define _GetR5(x) GetR5 x
#define _GetR6(x) GetR6 x
#define _GetR7(x) GetR7 x

#define _AddR0(x) AddR0 x
#define _AddR1(x) AddR1 x
#define _AddR2(x) AddR2 x
#define _AddR3(x) AddR3 x
#define _AddR4(x) AddR4 x
#define _AddR5(x) AddR5 x
#define _AddR6(x) AddR6 x
#define _AddR7(x) AddR7 x

#define _SubR0(x) SubR0 x
#define _SubR1(x) SubR1 x
#define _SubR2(x) SubR2 x
#define _SubR3(x) SubR3 x
#define _SubR4(x) SubR4 x
#define _SubR5(x) SubR5 x
#define _SubR6(x) SubR6 x
#define _SubR7(x) SubR7 x

//
// Timers
//
#define _SetTimer0(x) SetTimer0 x
#define _SetTimer1(x) SetTimer1 x
#define _SetTimer2(x) SetTimer2 x
#define _SetTimer3(x) SetTimer3 x

#define _GetTimer0(x) GetTimer0 x
#define _GetTimer1(x) GetTimer1 x
#define _GetTimer2(x) GetTimer2 x
#define _GetTimer3(x) GetTimer3 x

