from bs4 import BeautifulSoup as soup
try:
    from urllib.request import urlopen 
except ImportError: 
    from urllib2 import urlopen

filename = "products.csv"
f = open(filename,"w")
headers = "Status, Location, TeamA, TeamB, Batting_Team, Score_of_TeamA, Score_of_TeamB, Target, Updates\n"
f.write(headers)

print("Welcome to CricBuddy")
print("Do you want to watch live match or previous match")
print("Updating the scoreboard")

# names of all list required
batting_indicator = []  # batting team name
names_of_teams = []  # name of all the teams
updates = []  # commentry
target_needed = [] # overs+runs completed
team1_scores = []
team2_scores = []
status_of_match = [] # status of the match
test = 1
if test == 1:
    myurl = "https://www.espncricinfo.com/"
    uclient = urlopen(myurl)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html,"html.parser")

    containers = page_soup.find_all("div",{"class":"featured-scoreboard"})

    a = containers[0].find_all("div",{"class":"scorecard-container scorecard-with-separator"})

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
        name_team1 = team_1.div.p.text
    # name of team2
        team_2 = (team_1.find_all("div",{"class":"team"}))
        name_team2 = team_2[1].p.text
        print("Name of the teams "+name_team1+" VS "+name_team2)
    
        # batting indicator
        if status == "live":
            bb = a[i].find_all("div",{"class":"name-detail"})
            try:
                if bb[0].span.text == "":
                    batting_team = name_team1
                    print("name of the batting team : "+name_team1.replace(",","|"))
            except:
                batting_team = name_team2
                print("name of the batting team : "+name_team2.replace(",","|"))
        else:
            batting_team = "About to Begin"
            print("name of the batting team :"+"match yet to begin")

        # overs
        if status == "result":
            c = (team_1.find("div",{"class":"score-detail"}))
            score_a = c.text
            print("score of the "+name_team1+" is : "+c.text)

            # battting
            e = team_2[1].find("div",{"class":"score-detail"})
            d = e.find("span",{"class":"score"})
            score_b = d.text
            print("score of the "+name_team2+" is : "+d.text)
            target = "Match Over"

        elif status == "live":
            # bowling score of team1
            if bb[0].span.text == "":
                c = (team_1.find("div",{"class":"score-detail"}))
                score_a = (c.find("span",{"class":"score"}).text)
                print("score of the "+name_team1+" is : "+score_a)
                # batting score of team2
                d = team_2[0].find("div",{"class":"score-detail"})
#                print("ddddd",team_2[0])
                # target+overs
                target = (d.find("span",{"class":"score-info"}).text)
                print("target",target)
                print(" target to be acheived and overs completed "+target)
                score_b = "0"
            else:
                d = team_2[1].find("div",{"class":"score-detail"})
                # target+overs
                target = (d.find("span",{"class":"score-info"}).text)
                print("target",target)
                print(" target to be acheived and overs completed "+target)
                # runs made
                score_b = (d.find("span",{"class":"score"}).text)
                print("score of the "+name_team2+" is : "+score_b)

        comment = (a[i].find("div",{"class":"status-text"}))
        commentry = comment.span.text
        print("match updates : "+commentry.strip())

        f.write(status+","+location+","+name_team1+","+name_team2+","+batting_team+","+score_a+","+score_b+","+target+","+commentry+"\n")
    print()
    print()
    f.close()
else:
    print("Try again in 2 seconds")