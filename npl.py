#!/usr/bin/env python

#Copyright (C) 2009-2010 Johan Grip
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import array
import struct
import sys

##
## Statics
if sys.version_info < (2, 6):
    TRANSTAB = ''.join(chr(i) for i in range(256))
else:
    TRANSTAB = None

##
## Opcodes
##
OP_LOAD = 0     # Load a constand
OP_COMP = 1     # Comparisons
OP_FUNC = 2     # Function calls
OP_LABL = 4     # Label definition
OP_GOTO = 8     # Goto

##
## Compare operations
##
COMPARES = {
    4: "?",
    5: ">",
    6: "<",
    7: "=",
    10: "!="
}

##
## Functions
##
FUNCS = {
0:"Stop",
1:"True",
2:"False",
3:"Null",
4:"GetRandom",
5:"GetRandom10",
6:"GetRandom100",
7:"GetRandomTrueFalse",
8:"SetLevelCompleted",
9:"SetLevelFail",
10:"SetGameCompleted",
11:"SetGameFail",
12:"GetCrystalsPickedUp",
13:"GetCrystalsCurrentlyStored",
14:"GetCrystalsUsed",
15:"GetCrystalsStolen",
16:"SetMessage",
17:"GetR0",
18:"GetR1",
19:"GetR2",
20:"GetR3",
21:"GetR4",
22:"GetR5",
23:"GetR6",
24:"GetR7",
25:"SetR0",
26:"SetR1",
27:"SetR2",
28:"SetR3",
29:"SetR4",
30:"SetR5",
31:"SetR6",
32:"SetR7",
33:"AddR0",
34:"AddR1",
35:"AddR2",
36:"AddR3",
37:"AddR4",
38:"AddR5",
39:"AddR6",
40:"AddR7",
41:"SubR0",
42:"SubR1",
43:"SubR2",
44:"SubR3",
45:"SubR4",
46:"SubR5",
47:"SubR6",
48:"SubR7",
49:"SetMessagePermit",
50:"GetObjectiveShowing",
51:"GetTeleportIconClicked",
52:"GetMiniFiguresOnLevel",
53:"GetBuildIconClicked",
54:"SetBuildIconClicked",
55:"SetTeleportIconClicked",
56:"SetToolStoreIconClicked",
57:"GetToolStoreIconClicked",
58:"FlashToolStoreIcon",
59:"FlashBuildIcon",
60:"FlashTeleportIcon",
61:"SetGoBackIconClicked",
62:"GetGoBackIconClicked",
63:"FlashGoBackIcon",
64:"SetDigIconClicked",
65:"GetDigIconClicked",
66:"FlashDigIcon",
67:"GetTimer0",
68:"GetTimer1",
69:"GetTimer2",
70:"GetTimer3",
71:"SetTimer0",
72:"SetTimer1",
73:"SetTimer2",
74:"SetTimer3",
75:"GetBarracksBuilt",
76:"GetOreRefineriesBuilt",
77:"GetToolStoresBuilt",
78:"GetStudCount",
79:"GetTeleportsBuilt",
80:"GetMiniFigureSelected",
81:"GetSmallDiggerSelected",
82:"GetMiniFigureinSmallDigger",
83:"GetTrainFlags",
84:"SetTrainFlags",
85:"SetIconPos",
86:"SetIconSpace",
87:"SetIconWidth",
88:"SetMessageWait",
89:"GetMountIconClicked",
90:"SetMountIconClicked",
91:"FlashMountIcon",
92:"SetTutorialPointer",
93:"GetTutorialFlags",
94:"SetTutorialFlags",
95:"SetRockMonster",
96:"GetOrePickedUp",
97:"GetOreCurrentlyStored",
98:"GetOreUsed",
99:"GetOreStolen",
100:"GetCrystalRefineriesBuilt",
101:"FlashLayPathIcon",
102:"SetLayPathIconClicked",
103:"GetLayPathIconClicked",
104:"GetTeleportPadIconClicked",
105:"SetTeleportPadIconClicked",
106:"FlashTeleportPadIcon",
107:"GetMessageTimer",
108:"SetMessageTimerValues",
109:"GetTutorialBlockClicks",
110:"SetTutorialBlockClicks",
111:"GetTutorialCrystals",
112:"SetTutorialCrystals",
113:"GetPathsBuilt",
114:"GetTutorialBlockIsGround",
115:"SetCameraGotoTutorial",
116:"FlashDynamiteIcon",
117:"GetDynamiteClicked",
118:"SetDynamiteClicked",
119:"AddPoweredCrystals",
120:"GetGraniteGrinderSelected",
121:"GetChromeCrusherSelected",
122:"GetTutorialBlockIsPath",
123:"GetGunstationIconClicked",
124:"SetGunstationIconClicked",
125:"FlashGunstationIcon",
126:"GetGunstationsBuilt",
127:"SetOreAtIconPositions",
128:"GetVehicleTeleportsBuilt",
129:"GetVehicleTransportIconClicked",
130:"SetVehicleTransportIconClicked",
131:"FlashVehicleTransportIcon",
132:"GetUpgradeStationIconClicked",
133:"SetUpgradeStationIconClicked",
134:"FlashUpgradeStationIcon",
135:"GetUpgradeStationsBuilt",
136:"SetTutorialBlockIsGround",
137:"SetTutorialBlockIsPath",
138:"CameraLockOnObject",
139:"CameraUnlock",
140:"CameraZoomIn",
141:"CameraZoomOut",
142:"CameraRotate",
143:"GetCameraAtTutorial",
144:"GetSelectedRecordObject",
145:"GetSmallHelicopterSelected",
146:"GetRapidRiderSelected",
147:"GetMiniFigureinRapidRider",
148:"GetDismountIconClicked",
149:"SetDismountIconClicked",
150:"FlashDismountIcon",
151:"GetGetToolIconClicked",
152:"SetGetToolIconClicked",
153:"FlashGetToolIcon",
154:"GetAnyKeyPressed",
155:"SetPauseGame",
156:"GetGetLaserIconClicked",
157:"SetGetLaserIconClicked",
158:"FlashGetLaserIcon",
159:"SetRockMonsterAtTutorial",
160:"GetCallToArmsButtonClicked",
161:"GetRockMonstersDestroyed",
162:"SetGetPusherIconClicked",
163:"GetGetPusherIconClicked",
164:"FlashGetPusherIcon",
165:"GetRockMonsterRunningAway",
166:"SetCallToArms",
167:"FlashPowerStationIcon",
168:"SetPowerstationIconClicked",
169:"GetPowerstationIconClicked",
170:"GetPowerstationsBuilt",
171:"SetAttackDefer",
172:"SetRockMonsterPainThreshold",
173:"SetRockMonsterHealth",
174:"SetGameSpeed",
175:"FlashBarracksIcon",
176:"SetBarracksIconClicked",
177:"GetBarracksIconClicked",
178:"GetRecordObjectAtTutorial",
179:"GetHiddenObjectsFound",
180:"SetHiddenObjectsFound",
181:"GetOxygenLevel",
182:"FlashGeodomeIcon",
183:"GetGeodomeIconClicked",
184:"SetGeodomeIconClicked",
185:"GetGeodomeBuilt",
186:"AddStoredOre",
187:"GenerateSlug",
188:"GetSlugsOnLevel",
189:"GetMonstersOnLevel",
190:"SetCongregationAtTutorial",
191:"SetObjectiveSwitch",
192:"GetObjectiveSwitch",
193:"GetGraniteGrindersOnLevel",
194:"GetSmallDiggersOnLevel",
195:"GetDocksBuilt",
196:"GetRapidRidersOnLevel",
197:"GetUnitAtBlock",
198:"GetSmallHelicoptersOnLevel",
199:"GetRecordObjectAmountAtTutorial",
200:"AdvanceMessage",
201:"AllowCameraMovement",
202:"ClickOnlyObjects",
203:"ClickOnlyMap",
204:"ClickOnlyIcon",
205:"DisallowAll",
206:"SupressArrow",
207:"GetMiniFigureinGraniteGrinder",
208:"GetMiniFigureinChromeCrusher",
209:"GetMessagesAreUpToDate",
210:"SetCrystalPriority",
211:"MakeSomeoneOnThisBlockPickUpSomethingOnThisBlock",
212:"SetTrainIconClicked",
213:"GetTrainIconClicked",
214:"FlashTrainIcon",
215:"SetTrainDriverIconClicked",
216:"GetTrainDriverIconClicked",
217:"FlashTrainDriverIcon",
218:"SetTrainPilotIconClicked",
219:"GetTrainPilotIconClicked",
220:"FlashTrainPilotIcon",
221:"SetTrainSailorIconClicked",
222:"GetTrainSailorIconClicked",
223:"FlashTrainSailorIcon",
224:"GetSmallTruckSelected",
225:"GetMiniFigureinSmallTruck",
226:"GetMiniFigureinSmallHelicopter",
227:"SetBarracksLevel",
228:"SetDocksLevel",
229:"SetGeoDomeLevel",
230:"SetPowerstationLevel",
231:"SetToolStoreLevel",
232:"SetGunstationLevel",
233:"SetTeleportPadLevel",
234:"SetSuperTeleportLevel",
235:"SetUpgradeStationLevel",
236:"GetBarracksSelected",
237:"GetDocksSelected",
238:"GetGeoDomeSelected",
239:"GetPowerstationSelected",
240:"GetToolStoreSelected",
241:"GetGunstationSelected",
242:"GetTeleportPadSelected",
243:"GetSuperTeleportSelected",
244:"GetUpgradeStationSelected",
245:"SetUpgradeBuildingIconClicked",
246:"GetUpgradeBuildingIconClicked",
247:"FlashUpgradeBuildingIcon",
248:"GetBuildingsTeleported",
249:"SetBuildingsTeleported",
250:"CameraLockOnMonster",
251:"SetMonsterAttackPowerstation",
252:"ClickOnlyCalltoarms",
253:"FlashCallToArmsIcon",
254:"SetRecordObjectPointer",
255:"GetGetSonicBlasterIconClicked",
256:"SetGetSonicBlasterIconClicked",
257:"FlashGetSonicBlasterIcon",
258:"GetDropSonicBlasterIconClicked",
259:"SetDropSonicBlasterIconClicked",
260:"FlashDropSonicBlasterIcon",
261:"GetMonsterAtTutorial",
262:"SetMonsterAttackNowt",
263:"GetPlaceFenceIconClicked",
264:"SetPlaceFenceIconClicked",
265:"FlashPlaceFenceIcon",
266:"GetLevel1BarracksBuilt",
267:"GetLevel1DocksBuilt",
268:"GetLevel1GeodomeBuilt",
269:"GetLevel1PowerstationsBuilt",
270:"GetLevel1ToolStoresBuilt",
271:"GetLevel1GunstationsBuilt",
272:"GetLevel1TeleportsBuilt",
273:"GetLevel1VehicleTeleportsBuilt",
274:"GetLevel1UpgradeStationsBuilt",
275:"GetLevel2BarracksBuilt",
276:"GetLevel2DocksBuilt",
277:"GetLevel2GeodomeBuilt",
278:"GetLevel2PowerstationsBuilt",
279:"GetLevel2ToolStoresBuilt",
280:"GetLevel2GunstationsBuilt",
281:"GetLevel2TeleportsBuilt",
282:"GetLevel2VehicleTeleportsBuilt",
283:"GetLevel2UpgradeStationsBuilt",
284:"GetPoweredBarracksBuilt",
285:"GetPoweredDocksBuilt",
286:"GetPoweredGeodomeBuilt",
287:"GetPoweredPowerstationsBuilt",
288:"GetPoweredToolStoresBuilt",
289:"GetPoweredGunstationsBuilt",
290:"GetPoweredTeleportsBuilt",
291:"GetPoweredVehicleTeleportsBuilt",
292:"GetPoweredUpgradeStationsBuilt"
}

def disassemble(data):
    "Decompiles a NPL bytecode stream"
    import collections

    BYTECODE = struct.Struct('2H')
    result = ""
    bytecode = []
    labels = {}

    Instruction = collections.namedtuple("Instruction","address opcode operand")

    # Unpack instruction stream
    unpack = array.array('H',data)
    code = zip(unpack[1::2], unpack[::2])
    for address, data in enumerate(code):
        bytecode.append(Instruction(address,data[0],data[1]))
    # bytecode now contains the instruction stream

    # Pass one, collect the labels
    for op in bytecode:
        if op.opcode == OP_LABL:
            labels[op.address] = op.operand

    # Pass two, decompile
    for op in bytecode:
        label = ""
        if op.opcode == OP_LOAD:
            opcode = "LOAD"
            operand = str(op.operand)
        elif op.opcode == OP_COMP:
            opcode = "COMP"
            operand = COMPARES[op.operand]
        elif op.opcode == OP_FUNC:
            opcode = "FUNC"
            operand = FUNCS[op.operand]
        elif op.opcode == OP_LABL:
            label = "label%d:" % (op.operand)
            opcode = operand = ""
        elif op.opcode == OP_GOTO:
            opcode = "GOTO"
            operand = "label%d" % (labels[op.operand])
        else:
            opcode = "***Unknown opcode***"

        result += "%s\t%s %s\n" % (label, opcode, operand)

    # Done, return text
    return result

def assemble(source):
    "Compiles a bytecode assembly file into bytecode"
    BYTECODE = struct.Struct('2H')

    bytecode = array.array('H')

    # Pass one, massage the input
    cleansource = ""
    for line in source.splitlines():
        # Strip comments
        if ';' in line:
            line = line.partition(';')[0]
        # Remove whitespace
        line = line.strip()
        # Split labels into separate lines
        if ':' in line:
            label, colon, rest = line.partition(':')
            if rest != "":
                line = '%s:\n%s' % (label, rest.strip())
        # No blank lines:
        if line == "":
            continue
        cleansource += line + "\n"

    # Pass two, compile into bytecode
    labelidx = 0
    labels = {}
    gotos = {}
    for line in cleansource.splitlines():
        # Check for a label
        if ":" in line:
            label, colon, rest = line.partition(':')
            label = label.lower()       # Labels are case insensitive
            labels[label] = len(bytecode) // 2
            bytecode.append(labelidx)
            bytecode.append(OP_LABL)
            labelidx += 1
            continue
        opcode = line[0:4]
        operand = line[5:].strip()
        if opcode == "LOAD":
            bytecode.append(int(operand))
            bytecode.append(OP_LOAD)
        elif opcode == "COMP":
            if operand in COMPARES.values():
                for idx, op in COMPARES.iteritems():
                    if op == operand:
                        bytecode.append(idx)
                        bytecode.append(OP_COMP)
            else:
                raise ValueError("unknown compare function %s" % operand)
        elif opcode == "FUNC":
            if operand.lower() in [name.lower() for name in FUNCS.itervalues()]:
                found = False
                for idx, op in FUNCS.iteritems():
                    if op.lower() == operand.lower():
                        bytecode.append(idx)
                        bytecode.append(OP_FUNC)
                        found = True
                if not found:
                    raise ValueError("Could not find function index for %s" % (operand))
            else:
                raise ValueError("Calling unknown function %s" % operand)
        elif opcode == "GOTO":
            gotos[len(bytecode)] = operand
            bytecode.append(0)
            bytecode.append(OP_GOTO)
        else:
            raise ValueError("Unknown opcode encountered: %s" % opcode)

    # Pass three, fixup the GOTOs
    for addr, label in gotos.items():
        bytecode[addr] = labels[label.lower()]

    return bytecode.tostring()

def compile(source):
    "Compile .nrM source into bytecode"
    import re

    cleansource = ""
    datestamp = re.compile('"\d\d:\d\d:\d\d":')

    # Pass one, massage input
    for line in source.splitlines():
        # Remove whitespace
        line = line.strip()
        # Strip comments
        if ';' in line:
            line = line.partition(';')[0]
        if line.startswith('//'):
            continue
        # Ugly hack for that timestamp in the original files
        if datestamp.match(line):
            cleansource += "__init__:\n"
            continue
        # Remove brackets
        line = line.translate(TRANSTAB,'{}')
        # No blank lines:
        if line == "":
            continue
        cleansource += line + "\n"

    asmsource = ""
    # Pass two, tokenize and generate asm
    for token in cleansource.split():
        # Loading a constant
        if token.isdigit():
            opcode = "LOAD"
            operand = token
        # Label or goto
        elif ':' in token:
            if token.startswith(':'):
                # A goto
                opcode = "GOTO"
                operand = token[1:]
            else:
                # Label definition
                opcode = token
                operand = ''
        # Comparison
        elif token in COMPARES.values():
            opcode = "COMP"
            operand = token
        # Function call
        elif token.lower() in [name.lower() for name in FUNCS.itervalues()]:
            opcode = "FUNC"
            operand = token
        else:
            raise ValueError("Something wierd found: %s" % (token))
        # Add to asm source
        asmsource += "%s %s\n" % (opcode, operand)

    # Pass three, feed to compiler
    return assemble(asmsource)

if __name__ == "__main__":
    import optparse
    import os
    import sys

    parser = optparse.OptionParser(version="%prog 0.3")
    parser.add_option('-d', dest="disfile",
                    help="Disassemble a npl file")
    parser.add_option('-a', dest="asfile",
                    help="Assemble a npl file")
    parser.add_option('-c', dest="cfile",
                    help="Compile a nrM file")
    parser.add_option('-o', dest="output",
                    help="Specify output file. Defaults to console when disassembling, <asfile>.npl when assembling")
    options, args = parser.parse_args()

    # Check arguments
    if options.disfile is None and options.asfile is None and options.cfile is None:
        parser.print_help()
        sys.exit()

    if options.disfile is not None and options.asfile is not None and options.cfile is not None:
        print "Specify only one of -d, -a and -c."
        sys.exit()

    # Read source
    if options.asfile:
        data = open(options.asfile).read()
    elif options.disfile:
        data = open(options.disfile,'rb').read()
    elif options.cfile:
        if options.cfile == '-':
            data = sys.stdin.read()
        else:
            data = open(options.cfile).read()

    # Check output
    if options.disfile is not None:
        # Disassembling
        if options.output is not None:
            outfile = open(options.output,'w')
        else:
            outfile = sys.stdout
    if options.asfile is not None:
        # Assembling
        if options.output is not None:
            outfile = open(options.output,'wb')
        else:
            outfilename = options.asfile + ".npl"
            outfile = open(outfilename,'wb')
    if options.cfile is not None:
        # Compiling
        if options.output is not None:
            outfile = open(options.output,'wb')
        else:
            outfilename = options.cfile + ".npl"
            outfile = open(outfilename,'wb')

    # Do the work
    if options.asfile:
        result = assemble(data)
        outfile.write(result)
    if options.disfile:
        result = disassemble(data)
        outfile.write(result)
    if options.cfile:
        result = compile(data)
        outfile.write(result)

    # Done
