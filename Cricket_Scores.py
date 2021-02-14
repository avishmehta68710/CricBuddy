
from bs4 import BeautifulSoup as soup
try:
    from urllib.request import urlopen 
except ImportError: 
    from urllib2 import urlopen

filename = "scoreboards.xlsx"
files = "scoreboards.csv"
f = open(filename,"w")
f1 = open(files,"w")
headers = "Status, Location, TeamA, TeamB, Batting_Team, Score_of_TeamA, Score_of_TeamB, Target, Updates\n"
f.write(headers)
f1.write(headers)


print("Welcome to CricBuddy")
print("watch live match scores or previous match scores at CricBuddy")
print("Updating the scoreboard")
print("\n")

myurl = "https://www.espncricinfo.com/"
uclient = urlopen(myurl)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.find_all("div",{"class":"featured-scoreboard"})

a = containers[0].find_all("div",{"class":"scorecard-container scorecard-with-separator"})
score_a = "0"
score_b = "0"
target = "0"
batting_team = "Match yet to Begin"

for i in range(len(a)):
# status of the match
    status = a[i].div.div.div.text
    status = status.replace(",","|")
    print("Match Stauts : "+status)

# location of the match
    location = a[i].find("div",{"class":"description"}).text
    location = location.replace(",","|")
    print("location of the match : "+location.replace(",","|"))

# name of the team1
    team_1 = a[i].find("div",{"class":"teams"})
    name_team1 = team_1.div.p.text.replace(",","|")
# name of team2
    team_2 = (team_1.find_all("div",{"class":"team"}))
    name_team2 = team_2[1].p.text.replace(",","|")
    print("Name of the teams "+name_team1+" VS "+name_team2)
    
    # batting indicator
    if status == "live":
        bb = a[i].find_all("div",{"class":"name-detail"})
#        print(bb[0])
        try:
            if bb[0].span == "":
                batting_team = name_team1.replace(",","|")
                print("name of the batting team : "+name_team1.replace(",","|"))
        except:
            batting_team = name_team2.replace(",","|")
            print("name of the batting team : "+name_team2.replace(",","|"))
    else:
        batting_team = "About to Begin"
        print("name of the batting team :"+"match yet to begin")

# overs
    if status == "result":
        c = (team_1.find("div",{"class":"score-detail"}))
        score_a = c.text
        print("score of the "+name_team1+" is : "+c.text.replace(",","|"))

# battting
        e = team_2[1].find("div",{"class":"score-detail"})
        d = e.find("span",{"class":"score"})
        score_b = d.text
        print("score of the "+name_team2+" is : "+d.text.replace(",","|"))
        target = "Match Over"

    elif status == "live":
        # bowling score of team1
#        print(bb)
#        print(bb[0])
        if bb[0].span == "":
#            print(bb[0])
            c = (team_1.find("div",{"class":"score-detail"}))
            score_a = (c.find("span",{"class":"score"}).text)
            print("score of the "+name_team1+" is : "+score_a)
            # batting score of team2
            d = team_2[0].find("div",{"class":"score-detail"})
#                print("ddddd",team_2[0])
                # target+overs
            target = (d.find("span",{"class":"score-info"}).text.replace(",","|"))
            print("target",target)
            print(" target to be acheived and overs completed "+target)
        else:
            d = team_2[1].find("div",{"class":"score-detail"})
            # target+overs
            target = (d.find("span",{"class":"score-info"}).text.replace(",","|"))
            print("target",target)
            print(" target to be acheived and overs completed "+target)
            # runs made
            score_b = (d.find("span",{"class":"score"}).text.replace(",","|"))
            print("score of the "+name_team2+" is : "+score_b)



    comment = (a[i].find("div",{"class":"status-text"}))
    commentry = comment.span.text.replace(",","|")
    print("match updates : "+commentry.strip())

    f.write(status+","+location+","+name_team1+","+name_team2+","+batting_team+","+score_a+","+score_b+","+target+","+commentry+"\n")
    f1.write(status+","+location+","+name_team1+","+name_team2+","+batting_team+","+score_a+","+score_b+","+target+","+commentry+"\n")
        
print("\n")
f.close()
f1.close()
