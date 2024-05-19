import turtle as t
import pandas as p

myscr=t.Screen()
myscr.title("US STATE GAME")
img="blank_states_img.gif"
myscr.setup(width=700,height=700)
myscr.addshape(img)
t.shape(img)

# ans_state=myscr.textinput(title='Guess Country',prompt="Whats the another state's Name?").title()
statedata=p.read_csv("50_states.csv")
listofstate=statedata['state'].to_list()
loop=[]

while len(loop)<50:
    ans_state=myscr.textinput(title=f'{len(loop)}/50 States Correct',prompt="Whats the another state's Name?").title()
    print(ans_state)

    if ans_state in listofstate:
        loop.append(ans_state)
        corect=statedata[statedata['state']==ans_state]
        xx=int(corect['x'])
        yy=int(corect['y'])
        tt=t.Turtle()
        tt.hideturtle()
        tt.penup()
        tt.goto(x=xx,y=yy)
        tt.write(ans_state)
        # t.goto(x=xx,y=yy)
        # t.goto(x=,y=)


        
    if ans_state== 'E':
        notans=[i for i in listofstate if i not in loop]
        # for i in listofstate:
        #     if i not in loop:
                # notans.append(i)
        # print("\n\nNot Anwered States")
        # print(notans)
        notansweredstate={
            'State':notans
        }
        notdata=p.DataFrame(notansweredstate)
        notdata.to_csv("not_answered_states.csv")
        break


# t.mainloop()
