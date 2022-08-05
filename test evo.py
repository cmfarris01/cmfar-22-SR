import random

def org_generator(loci, size):  #size is number of organism in list
    org_list =[]
    for i in range(0,size):
        temp_list = []
        for j in range(0,loci):
            if random.random() > 0.5:
                temp_list.append(0)
            else:
                temp_list.append(1)
        org_list.append(temp_list)
    return(org_list)

def weighted_org_list(size, prop1, prop2, prop3, prop4):
    org_list =[]
    for i in range(0,size):
        temp_list = [0, 0, 0, 0]
        mut1 = random.randint(0,100)
        mut2 = random.randint(0,100)
        mut3 = random.randint(0,100)
        mut4 = random.randint(0,100)
        if mut1 <= prop1:
            temp_list[0] = 1
        if mut2 <= prop2:
            temp_list[1] = 1
        if mut3 <= prop3:
            temp_list[2] = 1
        if mut4 <= prop4:
            temp_list[3] = 1
        org_list.append(temp_list)
    return org_list

def ones_counter(org_list):
    count = 0
    for i in range(len(org_list)):
        count+= sum(org_list[i])
    return count

def evo_test(org_list, gens, mrate, drate):
    if gens==0:
        #print(org_list)
        #print(ones_counter(org_list))
        prop1=0
        prop2=0
        prop3=0
        prop4=0
        for m in range(0,len(org_list)):
            if org_list[m][0]==1:
                prop1+=1
            if org_list[m][1]==1:
                prop2+=1
            if org_list[m][2]==1:
                prop3+=1
            if org_list[m][3]==1:
                prop4+=1
        prop1 = int((prop1/len(org_list))*100)
        prop2 = int((prop2/len(org_list))*100)
        prop3 = int((prop3/len(org_list))*100)
        prop4 = int((prop4/len(org_list))*100)
        #print(prop1, prop2, prop3, prop4)
        return org_list
        
    else:
        #print(ones_counter(org_list))
        live_orgs = []
        for i in range(len(org_list)):
            mod = 1
            for j in range(4):
                mut = random.randint(0,100)
                if mut <= mrate:
                    if org_list[i][j]==0:
                        org_list[i][j]=1
                        mod*=0.9
                    elif org_list[i][j]==1:
                        org_list[i][j]=0
                elif mut > mrate:
                    if org_list[i][j]==1:
                        mod*=0.9
            live = random.randint(0,100)
            if live > drate*mod:
                live_orgs.append(org_list[i])
        
        prop1=0
        prop2=0
        prop3=0
        prop4=0
        #print(live_orgs)
        for m in range(0,len(live_orgs)):
            if live_orgs[m][0]==1:
                prop1+=1
            if live_orgs[m][1]==1:
                prop2+=1
            if live_orgs[m][2]==1:
                prop3+=1
            if live_orgs[m][3]==1:
                prop4+=1
        prop1 = int((prop1/len(live_orgs))*100)
        prop2 = int((prop2/len(live_orgs))*100)
        prop3 = int((prop3/len(live_orgs))*100)
        prop4 = int((prop4/len(live_orgs))*100)
        #print(prop1, prop2, prop3, prop4)
        next_gen = weighted_org_list(300, prop1, prop2, prop3, prop4)
        evo_test(next_gen, (gens-1), mrate, drate)

# Make mrate between 0 and 1 and use random.random() instead? 
def evo_hot(org_list, gens, mrate, drate):
    if gens==0:
        #print(org_list)
        #print(ones_counter(org_list))
        prop1=0
        prop2=0
        prop3=0
        prop4=0
        for m in range(0,len(org_list)):
            # prop1 += ( orglist[m][0] == 1 )
            # etc
            if org_list[m][0]==1:
                prop1+=1
            if org_list[m][1]==1:
                prop2+=1
            if org_list[m][2]==1:
                prop3+=1
            if org_list[m][3]==1:
                prop4+=1
        prop1 = int((prop1/len(org_list))*100)
        prop2 = int((prop2/len(org_list))*100)
        prop3 = int((prop3/len(org_list))*100)
        prop4 = int((prop4/len(org_list))*100)
        #print(prop1, prop2, prop3, prop4)
        return(org_list)
        
    else:
        #print(ones_counter(org_list))
        live_orgs = []
        for i in range(len(org_list)):
            mod = 1
            # Collapse all this into a for loop?
            # e.g.
            # mut = [ random.randint(0,100) for _ in range(4) ]
            # for j in range(0,4):
            #   if mut[j] <= mrate 
            #   ...
            mut1 = random.randint(0,100)
            mut2 = random.randint(0,100)
            mut3 = random.randint(0,100)
            mut4 = random.randint(0,100)
            if mut1 <= mrate:
                if org_list[i][0]==0:
                    org_list[i][0]=1
                    mod*=0.9
                elif org_list[i][0]==1:
                    org_list[i][0]=0
            elif mut1 > mrate:
                if org_list[i][0]==1:
                    mod*=0.9
            if mut2 <= mrate:
                if org_list[i][1]==0:
                    org_list[i][1]=1
                    mod*=0.9
                elif org_list[i][1]==1:
                    org_list[i][1]=0
            elif mut2 > mrate:
                if org_list[i][1]==1:
                    mod*=0.9
            if mut3 <= mrate:
                if org_list[i][2]==0:
                    org_list[i][2]=1
                    mod*=1.111
                elif org_list[i][2]==1:
                    org_list[i][2]=0
            elif mut3 > mrate:
                if org_list[i][2]==1:
                    mod*=1.111
            if mut4 <= mrate:
                if org_list[i][3]==0:
                    org_list[i][3]=1
                    mod*=1.111
                elif org_list[i][3]==1:
                    org_list[i][3]=0
            elif mut4 > mrate:
                if org_list[i][3]==1:
                    mod*=1.111

            live = random.randint(0,100)
            if live > drate*mod:
                # Clone of org_list[i]?  I don't think that it matters
                # here, but make sure that you know the difference
                # between this line and 
                # live_orgs.append(org_list[i].copy())
                live_orgs.append(org_list[i])
        
        prop1=0
        prop2=0
        prop3=0
        prop4=0
        #print(live_orgs)
        for m in range(0,len(live_orgs)):
            if live_orgs[m][0]==1:
                prop1+=1
            if live_orgs[m][1]==1:
                prop2+=1
            if live_orgs[m][2]==1:
                prop3+=1
            if live_orgs[m][3]==1:
                prop4+=1
        prop1 = int((prop1/len(live_orgs))*100)
        prop2 = int((prop2/len(live_orgs))*100)
        prop3 = int((prop3/len(live_orgs))*100)
        prop4 = int((prop4/len(live_orgs))*100)
        #print(prop1, prop2, prop3, prop4)
        next_gen = weighted_org_list(300, prop1, prop2, prop3, prop4)
        # Also, you might want to try to rewrite evo_hot
        # "unrecursively".  Platforms have an upper limit for how deep
        # your recursions go.  Check sys.getrecursionlimit() on your
        # system.  On mine the limit is 1000.  This means that if gens
        # > 1000 I'd get a recursion error.
        #
        # If I was writing this, I'd make evo_hot do one step like 
        #
        # next_gen = evo_hot_1_step(curr_gen,mrate,drate)
        #
        # Then define evo_hot as
        #
        # def evo_hot(curr_gen,gens,mrate,drate):
        #   for _ in range(gens - 1):
        #       curr_gen = evo_hot_1_step(curr_gen,mrate,drate)
        #   return curr_gen
        #
        return evo_hot(next_gen, (gens-1), mrate, drate)

def evo_cold(org_list, gens, mrate, drate):
    if gens==0:
        #print(org_list)
        #print(ones_counter(org_list))
        prop1=0
        prop2=0
        prop3=0
        prop4=0
        for m in range(0,len(org_list)):
            if org_list[m][0]==1:
                prop1+=1
            if org_list[m][1]==1:
                prop2+=1
            if org_list[m][2]==1:
                prop3+=1
            if org_list[m][3]==1:
                prop4+=1
        prop1 = int((prop1/len(org_list))*100)
        prop2 = int((prop2/len(org_list))*100)
        prop3 = int((prop3/len(org_list))*100)
        prop4 = int((prop4/len(org_list))*100)
        #print(prop1, prop2, prop3, prop4)
        return org_list
        
    else:
        #print(ones_counter(org_list))
        live_orgs = []
        for i in range(len(org_list)):
            mod = 1
            mut1 = random.randint(0,100)
            mut2 = random.randint(0,100)
            mut3 = random.randint(0,100)
            mut4 = random.randint(0,100)
            if mut1 <= mrate:
                if org_list[i][0]==0:
                    org_list[i][0]=1
                    mod*=1.111
                elif org_list[i][0]==1:
                    org_list[i][0]=0
            elif mut1 > mrate:
                if org_list[i][0]==1:
                    mod*=1.111
            if mut2 <= mrate:
                if org_list[i][1]==0:
                    org_list[i][1]=1
                    mod*=1.111
                elif org_list[i][1]==1:
                    org_list[i][1]=0
            elif mut2 > mrate:
                if org_list[i][1]==1:
                    mod*=1.111
            if mut3 <= mrate:
                if org_list[i][2]==0:
                    org_list[i][2]=1
                    mod*=0.9
                elif org_list[i][2]==1:
                    org_list[i][2]=0
            elif mut3 > mrate:
                if org_list[i][2]==1:
                    mod*=0.9
            if mut4 <= mrate:
                if org_list[i][3]==0:
                    org_list[i][3]=1
                    mod*=0.9
                elif org_list[i][3]==1:
                    org_list[i][3]=0
            elif mut4 > mrate:
                if org_list[i][3]==1:
                    mod*=0.9

            live = random.randint(0,100)
            if live > drate*mod:
                live_orgs.append(org_list[i])
        
        prop1=0
        prop2=0
        prop3=0
        prop4=0
        #print(live_orgs)
        for m in range(0,len(live_orgs)):
            if live_orgs[m][0]==1:
                prop1+=1
            if live_orgs[m][1]==1:
                prop2+=1
            if live_orgs[m][2]==1:
                prop3+=1
            if live_orgs[m][3]==1:
                prop4+=1
        prop1 = int((prop1/len(live_orgs))*100)
        prop2 = int((prop2/len(live_orgs))*100)
        prop3 = int((prop3/len(live_orgs))*100)
        prop4 = int((prop4/len(live_orgs))*100)
        #print(prop1, prop2, prop3, prop4)
        next_gen = weighted_org_list(300, prop1, prop2, prop3, prop4)
        evo_cold(next_gen, (gens-1), mrate, drate)

first_list = org_generator(4, 300)            

def trunc_print(x):
    """ This function just truncates print's output.  Change `trunc'
    to False to turn it off """
    x = str(x)
    dots = ""
    if len(x) > 70:
        dots=" . . ."
    __builtins__.print(x[:70]+dots)

# Change `trunc' to False to avoid truncating
trunc = True
if trunc:
    print = trunc_print

print(first_list)
print(ones_counter(first_list))
print("break")
final_list = evo_hot(first_list, 100, 20, 50)
print(ones_counter(first_list))
print(final_list)

post_hot =[[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 
1], [1, 0, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 
0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 
0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1], [0, 1, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1], 
[1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 0, 1, 1], [1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 1, 
0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [1, 0, 
1, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 
0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [1, 1, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0], 
[0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 0, 0, 1], [1, 1, 0, 
1], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1]]
#64 57 48 45
