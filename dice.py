import statistics
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

dice_result=[]
for i in range (0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice=dice1+dice2
    dice_result.append(dice)

#calculating mean ,median, mode and sd
mean=statistics.mean(dice_result)
mode=statistics.mode(dice_result)
median=statistics.median(dice_result)
sd=statistics.stdev(dice_result)
print("mean:",mean)
print("mode:",mode)
print("median:",median)
print("standard deviation:",sd)

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="sd3"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="sd3"))
fig.show()