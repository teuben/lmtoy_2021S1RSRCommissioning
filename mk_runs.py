#! /usr/bin/env python
#
#   script generator for RSR linechecks
#
#   lmtinfo.py grep LineCheck Bs

import os
import sys

from lmtoy import runs

#  2022S1RSRCommissioning  2018S1RSRCommissioning 2018ARSRCommissioning
#  2014ARSRCommissioning   2015ARSRCommissioning  2016ARSRCommissioning
#  2014A
project="linecheck"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['I10565'] = [94687, 94688,
                95132, 95186, 95187, 95234, 95235, 98306, 98307,
                98557, 98558,
                99815, 99816, 99820, 99821, 99846, 99847, 99947, 99948, 100384, 100385]                # 2022-03-02 to 2022-05-19

# historic 50m data pre-pandemic (2018, 2020) - jan 2018 50m was installed
on['I10565h50'] = [71588, 71589, 71590, 71605, 71606, 71610, 71611, 74021, 74022, 74051, 74052,        # 2018A   2018-02-10 to 2018-03-24
                   76707, 76708, 76829, 76830, 76988, 76989, 76991, 76992, 77008, 77009,               # 2018S1  2018-05-18 to 2018-06-09
                   77113, 77114, 77420, 77421, 
                   92057, 92060, 92061, 92062, 92064, 92065, 92067, 92068]                             # 2018S1  2020-03-05 

# historic 32m data
on['I10565h32'] = [28190 , 28191 , 29674 , 29675 , 31349 , 31350 , 31524 , 31525 , 31528 , 31529 ,
                   31532 , 31533 , 32018 , 32019 , 32876 , 32877 , 32992 , 32993 , 33392 , 33393 ,
                   33543 , 33544 , 33546 , 33547 , 33551 , 33552 , 33848 , 33849 , 33905 , 33906 ,
                   34431 , 34432 , 34788 , 34789 , 35691 , 35692 , 36445 , 36446 , 36949 , 36950 ,
                   38494 , 38495 , 38624 , 38625 , 38776 , 38777 , 39593 , 39594 , 39677 , 39678 ,
                   39682 , 39683 , 39686 , 39687 , 40134 , 40135 , 40286 , 40287 , 40605 , 40606 ,
                   40608 , 40609 , 40797 , 40798 , 41194 , 41195 , 41197 , 41198 , 42166 , 42167 ,
                   42303 , 42304 , 42313 , 42314 , 42318 , 42319 , 42864 , 42865 , 49515 , 49516 ,
                   52195 , 52196 , 54693 , 54694 , 54802 , 54803 , 55514 , 55515 , 55770 , 55771 ,
                   55784 , 55785 , 57632 , 57633 , 58383 , 58384 , 58392 , 58393 , 58448 , 58449 ,
                   58452 , 58618 , 58619 , 58620 , 58731 , 58732 , 58829 , 58830 , 58842 , 58843 ,
                   58866 , 58867 , 58962 , 58963 , 59035 , 59036 , 59112 , 59113 , 59122 , 59123 ,
                   59257 , 59258 , 59359 , 59360 , 59399 , 59400 , 59470 , 59471 , 59951 , 59952 ,
                   60125 , 60126 , 60977 , 60978 , 61087 , 61088 , 61218 , 61219 , 61352 , 61353 ,
                   61507 , 61508 , 61510 , 61511 , 61513 , 61514 , 61581 , 61582 , 61696 , 61697 ,
                   61827 , 61828 , 61978 , 61979 , 66008 , 66009 , 66175 , 66176 , 66236 , 66237 ,
                   66382 , 66383 , 66894 , 66895 , 66965 , 66966 , 67130 , 67131 , 67178 , 67179 ,
                   67310 , 67311 , 67312 , 67412 , 67413 , 67438 , 67439 , 67441 , 67442 , 67641 ,
                   67642 , 67772 , 67773 , 67899 , 67900 , 67964 , 67965 , 67968 , 67969 , 68397 ,
                   68398 , 68408 , 68409 , 68476 , 68477 , 68553 , 68554 , 68632 , 68633]

on['I12112'] = [94993, 94994, 95302, 95303,
                98184, 98185, 98299, 98300, 98302, 98303,              
                98422, 98423]

on['I12112h50'] = [71635, 71636, 72977, 72978, 73749, 73750, 73939, 73940, 75152, 75153,               # 2018A
                   76288, 76289, 76579, 76580, 76712, 76713, 76879, 76880, 77013, 77014, 77118, 77119, # 2018S1
                   92071, 92072, 92074, 92075, 92077, 92078, 92080, 92081, 92083, 92084, 92086, 92087] # taken in 2020

# 2014-11-15
on['I12112h32'] = [28383, 28384, 28488, 28489, 29088, 29089, 29251, 29252, 29372, 29373,
                   29521, 29522, 34099, 34100, 35393, 35394, 35657, 35658, 35863, 35864,
                   35984, 35985, 35990, 35991, 36192, 36193, 36364, 36365, 36641, 36642,
                   36832, 36833, 36911, 36912, 37025, 37026, 37416, 37417, 37533, 37534,
                   38337, 38338, 38558, 38559, 38633, 38634, 38787, 38788, 38790, 38791,
                   39364, 39365, 39485, 39486, 39624, 39625, 39666, 39667, 39696, 39697,
                   39919, 39920, 40219, 40220, 40586, 40587, 40597, 40598, 40617, 40618,
                   40703, 40704, 40789, 40790, 40792, 40793, 40990, 40991, 41070, 41071,
                   41080, 41081, 41148, 41149, 41207, 41208, 41218, 41219, 41223, 41224,
                   41324, 41325, 41476, 41477, 41518, 41519, 41594, 41595, 41741, 41742,
                   41813, 41814, 41933, 41934, 42056, 42057, 42066, 42067, 42071, 42072,
                   42338, 42339, 42446, 42447, 42597, 42598, 42809, 42810, 42958, 42959,
                   43036, 43037, 43161, 43162, 43285, 43286, 43288, 43289, 43694, 43695,
                   43699, 43700, 43709, 43710, 44176, 44177, 44338, 44339, 44343, 44344,
                   44397, 44398, 44414, 44415, 44476, 44477, 44630, 44631, 44790, 44791,
                   44882, 44883, 44975, 44976, 45086, 45087, 45146, 45147, 45274, 45275,
                   45332, 45333, 45335, 45336, 45456, 45457, 45571, 45572, 45657, 45658,    # 2015-06-30T
                   45718, 53523, 53524, 54387, 54388, 54518, 54519, 54704, 54705, 55049,
                   55050, 55192, 55193, 55336, 55337, 55498, 55499, 55839, 55840, 55990,
                   55991, 56170, 56171, 56278, 56279, 56340, 56341, 57595, 57596, 58344,
                   58345, 58348, 58349, 59158, 59159, 59161, 59162, 59169, 59170, 59309,
                   59310, 59634, 59635, 59637, 59638, 59671, 59672, 61883, 61884, 61975,    # 2016-04-17
                   61976, 62019, 62020, 65624, 65625, 65627, 65628, 66665, 66666, 66810,
                   66811, 67498, 67499, 67569, 67570]                                       # 2017-02-17


on['I17208'] = [95306, 95307,  95524,  95525,  98594,  98595,  98649,  98650,
                99862, 99863, 100070, 100071, 100309, 100310, 100427, 100428]

on['I17208h50'] = [76304, 76305, 76307, 76308, 76310, 76311, 77439, 77440, 78136, 78137]               # 2018S1 (none in 2018A)

on['I17208h32'] = [37605, 37606, 40757, 40758, 40873, 40874, 41280, 41281, 41383, 41384,
                   41525, 41526, 41708, 41709, 41753, 41754, 41950, 41951, 42027, 42028,
                   42267, 42268, 42407, 42408, 42554, 42555, 42722, 42723, 42920, 42921,
                   42965, 42966, 43102, 43103, 43232, 43233, 43436, 43437, 43520, 43521,
                   43608, 43611, 43613, 43624, 43625, 43769, 43770, 44267, 44268, 44435,     # 2014A 
                   44436, 44500, 44501, 44581, 44582, 44672, 44673, 58158, 58159, 58312,
                   58313, 58918, 58919, 59056, 59057, 59458, 59459, 59596, 59597, 59742,
                   59743, 59940, 59941, 60070, 60071, 61549, 61550, 61955, 61956, 62077,     # 2015A
                   62078, 65954, 65955]

# oops, this one repeated in 2023S1
on['I05189'] = [106684, 106683, 106168, 106167, 106003, 106002, 105391, 105390, 105384, 105383,
                105233, 105232, 104912, 104911, 104786, 104785, 104660, 104659, 104532, 104531,
                104426, 104425, 103714, 103713, 103510, 103509, 103419, 103418, 103381, 103380,
                103373, 103372]

# not sure if this is 50m or 32m, check please
on['I05189h50'] = [71553, 71552]

on['I05189h32'] = [67958, 67957, 67034, 67033, 66747, 66746, 66590, 66589, 66510, 66509,
                   66227, 66226, 66072, 66071, 65972, 65971, 65810, 65809, 65646, 65645,
                   58833, 58832, 58174, 58173, 58024, 58023, 57868, 57867, 57157, 57156,
                   56944, 56943, 56838, 56837, 56703, 56702, 56587, 56586, 56352, 56351,
                   56210, 56209, 56154, 56153, 56151, 56150, 56003, 56002, 55852, 55851,
                   55358, 55357, 55207, 55206, 55062, 55061, 54935, 54934, 54628, 54627,
                   54425, 54424, 53594, 53593, 53536, 53535, 53312, 53311, 53165, 53164,
                   53049, 53048, 52986, 52985, 52915, 52914, 52726, 52725, 52579, 52578,
                   52455, 52454, 52287, 52286, 52228, 52227, 52097, 52096, 52007, 52006,
                   51820, 51819, 51647, 51646, 51344, 51343, 50442, 50441, 50217, 50216,
                   50205, 50204, 50186, 50185, 50174, 50173, 50163, 50162, 50152, 50151,
                   50036, 50035, 49940, 49939, 38245, 38244, 37087, 37086, 36853, 36852,
                   36684, 36683, 36559, 36558, 36387, 36386, 36231, 36230, 36221, 36220,
                   36215, 36214, 36048, 36047, 35907, 35906, 35758, 35757, 35756, 35541,
                   35540, 35290, 35289, 34678, 34677, 34502, 34501, 34499, 34498, 34264,
                   34263, 34177, 34176, 33783, 33782, 33664, 33663, 33199, 33198, 32944,
                   32943, 32096, 32095, 31393, 31392, 31236, 31235, 31106, 31105, 30989,
                   30988, 30850, 30849, 30236, 30235, 30113, 30112, 29980, 29979, 29853,
                   29852, 29753, 29752, 29545, 29544, 29446, 29445, 29313, 29312, 29163,
                   29162, 28860, 28859, 28709, 28708, 28149, 28148, 28130, 28129, 28092,
                   28091]


# 101100 and 101099 for I23365


#  doesn't seem to work too well
#on['mwc349a'] = [98534, 98535, 100114, 100114, 101103, 101104, 101106, 101107]


#       common parameters per source on the first dryrun (run1, run2)
pars1 = {}

pars1['I10565']     = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I10565h50']  = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I10565h32']  = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I12112']     = "xlines=107.40,0.25"
pars1['I12112h50']  = "xlines=107.40,0.25"
pars1['I12112h32']  = "xlines=107.40,0.25"
pars1['I17208']     = "xlines=110.50,0.20,108.8,0.3"
pars1['I17208h50']  = "xlines=110.50,0.20,108.8,0.3"
pars1['I17208h32']  = "xlines=110.50,0.20,108.8,0.3"
pars1['I05189']     = "xlines=110.53,0.20"
pars1['I05189h50']  = "xlines=110.53,0.20"
pars1['I05189h32']  = "xlines=110.53,0.20"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['I10565']     = ""
pars2['I10565h50']  = ""
pars2['I10565h32']  = ""
pars2['I12112']     = ""
pars2['I12112h50']  = ""
pars2['I12112h32']  = ""
pars2['I17208']     = ""
pars2['I17208h50']  = ""
pars2['I17208h32']  = ""
pars2['I05189']     = ""
pars2['I05189h50']  = ""
pars2['I05189h32']  = ""

# below here no need to change code
# ========================================================================

#        helper function for populating obsnum dependant argument -- deprecated
def getargs3(obsnum):
    """ search for <obsnum>.args
    """
    f = "%d.args" % obsnum
    if os.path.exists(f):
        lines = open(f).readlines()
        args = ""
        for line in lines:
            if line[0] == '#': continue
            args = args + line.strip() + " "
        return args
    else:
        return ""

#        specific parameters per obsnum will be in files <obsnum>.args -- deprecated
pars3 = {}
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        pars3[o] = getargs3(o)

#        obsnum.args is alternative single file pars file to set individual parameters
pars4 = {}
if os.path.exists("obsnum.args"):
    lines = open("obsnum.args").readlines()
    for line in lines:
        if line[0] == '#': continue
        w = line.split()
        pars4[int(w[0])] = w[1:]
        print('PJT',w[0],w[1:])

def getargs(obsnum):
    """ search for <obsnum> in obsnum.args
    """
    args = ""
    if obsnum in pars4.keys():
        print("PJT2:",obsnum,pars4[obsnum])
        for a in pars4[obsnum]:
            args = args + " " + a
    return args

run1  = '%s.run1'  % project
run1a = '%s.run1a' % project
run1b = '%s.run1b' % project
run2  = '%s.run2' % project
run2a = '%s.run2a' % project

fp1 = open(run1,  "w")
fp2 = open(run1a, "w")
fp3 = open(run1b, "w")

fp4 = open(run2,  "w")
fp5 = open(run2a, "w")

#                           single obsnum
n1 = 0
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        cmd1 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1 %s %s" % (o,s,pars1[s], pars2[s], getargs(o))
        cmd2 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1" % (o,s,pars1[s])
        cmd3 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 %s" % (o,s,pars2[s], getargs(o))
        fp1.write("%s\n" % cmd1)
        fp2.write("%s\n" % cmd2)
        fp3.write("%s\n" % cmd3)
        n1 = n1 + 1

#                           combination obsnums
n2 = 0        
for s in on.keys():
    obsnums = ""
    n3 = 0
    for o1 in on[s]:
        o = abs(o1)
        if o1 < 0: continue
        n3 = n3 + 1
        if obsnums == "":
            obsnums = "%d" % o
        else:
            obsnums = obsnums + ",%d" % o
    print('%s[%d/%d] :' % (s,n3,len(on[s])), obsnums)
    cmd4 = "SLpipeline.sh _s=%s admit=0 restart=1 obsnums=%s" % (s, obsnums)
    cmd5 = "SLpipeline.sh _s=%s admit=1 srdp=1  obsnums=%s" % (s, obsnums)
    fp4.write("%s\n" % cmd4)
    fp5.write("%s\n" % cmd5)
    n2 = n2 + 1

print("A proper re-run of %s should be in the following order:" % project)
print(run1a)
print(run2)
print(run1b)
print(run2a)
print("Where there are %d single obsnum runs, and %d combination obsnums" % (n1,n2))

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
