#hw11.py
#kalynn kosyka

#suppose to analyze csv file that everyone in CSC111 had contributed that included category, name, color, pair programmers, quadrant, coordinates
#take the information and get the valid lines and draw out the polygons(buildings, trees, etc)
#compare each building to a csv file that contains the year the building has been constructed with the name of the building
#each item, if it is in the date-building csv file, those buildings are color coded based on construction date
#if the item is not in date-building csv file, will color code differenly based on category
#when drawing the buildings, there should be no overlaps
#recreate smith map

##Note: version 5

#libraries
from graphics import*

#global variables/lists
WIDTH = 875
HEIGHT = 730

win = GraphWin( "Kosyka - Smith Map", WIDTH, HEIGHT)

MapCSV = "GroupSmithMap.csv"
DatesCSV = "SmithConstructionDates.csv"

#lists used to help with filtering out unnecessary items, list created through other programs
colors = ['aliceblue', 'antiquewhite', 'antiquewhite2', 'antiquewhite3', 'antiquewhite4', 'aquamarine', 'azure', 'beige',
          'bisque', 'bisque2', 'bisque3', 'bisque4', 'black', 'black', 'blanchedalmond', 'blue', 'blue', "blues',''", 'blueviolet',
          'brown', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'colorname', 'coral', 'cornflowerblue',
          'cornsilk', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey',
          'darkkhaki', 'darkolivegreen', 'darkorange', 'darkorchid', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray',
          'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick', 'floralwhite',
          'forestgreen', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'grey49',
          'honeydew', 'honeydew2', 'honeydew3', 'honeydew4', 'hotpink', 'indianred', 'ivory', 'ivory2', 'ivory3', 'ivory4', 'khaki',
          'lavender', 'lavenderblue', 'lavenderblush', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
          'lightcyan', 'lightgoldenrod', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon',
          'lightseagreen', 'lightskyblue', 'lightslateblue', 'lightslategray', 'lightsteelblue', 'lightyellow', 'limegreen',
          'limegreen', 'linen', 'maroon', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
          'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
          'mintcream', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olivedrab', 'orange', 'orangered',
          'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'papayawhip', 'peachpuff',
          'peachpuff2', 'peachpuff3', 'peachpuff4', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'red', 'rosybrown',
          'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'sandybrown', 'seagreen', 'seashell', 'seashell2', 'seashell3',
          'seashell4', 'sienna', 'skyblue', 'slateblue', 'slategray', 'snow', 'snow2', 'snow3', 'snow4', 'springgreen', 'steelblue',
          'tan', 'thistle', 'tomato', 'turquoise', 'violet', 'violetred', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

validItems = ['138elmhouse', '146elm', '150elmhouse', '150elmstreet', '30belmontavenue', '44greenstreet', '76elmstreet',
              'admissionoffice', 'admissionsparking', 'ainsworthgymnasium', 'basshall', 'bedfordterrace', 'belmontavenue',
              'bigtree', 'boathouse', 'botanicalgardens', 'botanicalpond', 'botanicgardenpond', 'botanicgardens', 'burtonhall',
              'campuscenter', 'capenannex', 'capengarden', 'capenhouse', 'chapelparking', 'chapinhouse', 'chapinlawn', 'chapinway',
              'chasehouse', 'clarkhall', 'collegehall', 'collegelane', 'comstockhouse', 'conferencecenter', 'conwayhouse', 'courts',
              'courts', 'crewhouse', 'cushinghouse', 'daviscenter', 'davisparking', 'daweshouse', 'deweyhall', 'drewhall', 'dryadsgreen',
              'eleanorducketthouse', 'ellenemersonhouse', 'elmst', 'elmst', 'elmst1', 'field', 'field', 'fieldhouse', 'fieldhouseparking',
              'fordhall', 'fordparking', 'franklinkinghouse', 'friedmancomplex', 'friedmanparking', 'gables', 'garage', 'gardinerhouse',
              'garrisonhall', 'gilletthouse', 'grecourtparking', 'greenbox', 'greenst', 'greenstreet', 'hatfieldhall', 'havenhouse',
              'helenhillshillschapel', 'helenhillshillsparking', 'henshawavenue', 'hillyerhall', 'hopkinshouse', 'hubbardhouse',
              'indoortrackparkinglot', 'johnmgreenehall', 'jordanhouse', 'jostenlibrary', 'lamontbridge', 'lamonthouse', 'lamontparking',
              'laurascaleshouse', 'lawrencehouse', 'lillyhall', 'lymanconservatory', 'mandelleroad', 'marthawilsonhouse', 'mcconnellhall',
              'mendenhall', 'morganhall', 'morrishouse', 'morrowhouse', 'neilsondr', 'neilsonlibrary', 'nielsondr', 'northrophouse',
              'otheravenue', 'othertree', 'outdoortrack', 'outdoortrack', 'p', 'p1', 'p2', 'p3', 'paradisepond', 'paradisepondextended',
              'paradiseroad', 'park', 'parkannex', 'parkhouse', 'parking', 'parking1', 'parking10', 'parking11', 'parking2', 'parking3',
              'parking4', 'parking5', 'parking6', 'parking7', 'parking8', 'parking9', 'parkingarea', 'parkinggarage', 'parkinglot',
              'parkingneartenniscourts', 'parkingonweststreet', 'parsonsannex', 'parsonshouse', 'piercehall', 'pitch', 'presidentshouse',
              'prospectstreet', 'queenstreet', 'roadsinsidecampus', 'roadsinsidecampus', 'roundhillroad', 'sabinreedhall', 'sagehall',
              'scaleshouse', 'schachtcenterforhealthandwellness', 'scottgymnasium', 'seelyehall', 'seelyelawn', 'sessionsannex',
              'sessionshouse', 'softballfield', 'softballfield', 'stoddardhall', 'sweeneyconcerthall', 'talbothouse', 'tenneyhouse',
              'tennis', 'tennis', 'tenniscourt', 'theaterparking', 'theatre14', 'thegables', 'thepitch', 'tree', 'trees', 'trees1',
              'trees2', 'trees3', 'tylerannex', 'tylerhouse', 'unityhouse', 'washburnhouse', 'wesleyhouse', 'weststreet', 'wilderhouse',
              'wrighthall', 'youngsciencelibrary', 'ziskindhouse']

validCategories = ["field", "lawn", "parkinglot", "river", "road", "tree", "building", "house"] # not including buildings, houses ,#"building", "field", "parkinglot", "river", "road", "house", "tree"

validHouses = ['albright', 'alumnae', 'baldwin', 'capenannex', 'chapen', 'chapin', 'chase', 'comstock', 'cushing', 'cutter',
               'duckett', 'emerson', 'gardiner', 'gillett', 'hopkins', 'jordan', 'king', 'lamont', 'lawrence', 'lymanplant',
               'morris', 'morrow', 'northrop', 'park', 'parsonsannex', 'scales', 'sessions', 'sessionsannex', 'talbot', 'tenney',
               'tyler', 'washburn', 'wesley', 'wilder', 'wilson', 'ziskind']

               
#############################################################################################
#
#                             CLASSES
#
#############################################################################################

class colorCoding:
     #purpose is to create little boxes that are used for color coding, or anything associated to the color coding
     
     def __init__(self, x1, y1, x2, y2, color, text):
          p1 = Point(x1, y1)
          p2 = Point(x2, y2)
          self.frame = Rectangle(p1, p2)
          self.frame.setFill(color)
          self.label= Text(Point( x1+75, y1+15), text)
        
     def draw(self, win):
          self.frame.draw( win )
          self.label.draw( win )

     def setWidth(self, win):
          self.frame.setWidth(win)

     def setStyle(self, win):
          self.frame.setStyle(win)

     def setSize(self, win):
          self.frame.setSize(win)


        
#########################################################################
#
#                            FUNCTIONS
#
##########################################################################

def lengend():
     #to create the legend that appears on the right side of the map
     x1 = 745
     y1 = 240
     x2 = 775
     y2 = 270

     outlineBox  = colorCoding(4,4,735,730, "", "")
     outlineBox.setWidth(8)
     outlineBox.draw(win)
     titleBox = colorCoding(740, 4, 875, 190, "white", "")
     titleBox.draw(win)
     title = Text (Point(808, 100), "SMITH \n COLLEGE \n MAP")
     title.setSize(28)
     title.setStyle("bold")
     title.draw(win)
     
     backgroundBox = colorCoding(740, 195, 873, 725 , "white", "")
     lengendLabel = Text (Point(808, 215), "LEGEND")
     lengendLabel.setStyle('bold')
     descriptionLabel = Text (Point(807, 230), "(year building constructed)")
     backgroundBox.draw(win)
     lengendLabel.draw(win)
     descriptionLabel.draw(win)
     box1 = colorCoding(x1, y1, x2, y2, "thistle", "1700 - 1750")
     box1.draw(win)
     box2 = colorCoding(x1, y1+35, x2, y2+35, "purple", "1750 - 1800")
     box2.draw(win)
     box3 = colorCoding(x1, y1+70, x2, y2+70, "violet", "1800 - 1850")
     box3.draw(win)
     box4 = colorCoding(x1, y1+105, x2, y2+105, "darkviolet", "1850 - 1900")
     box4.draw(win)
     box5 = colorCoding(x1, y1+140, x2, y2+140, "mediumorchid", "1900 - 1950")
     box5.draw(win)
     box6 = colorCoding(x1, y1+175, x2, y2+175, "orchid", "1950 - 2000")
     box6.draw(win)
     box7 = colorCoding(x1, y1+210, x2, y2+210, "mediumvioletred", "2000 - Present")
     box7.draw(win)
     box8 = colorCoding(x1, y1+245, x2, y2+245, "red", "Unknown Year")
     box8.draw(win)
     
     categoryLabel = Text (Point(808, 530), "(category)")
     categoryLabel.draw(win)
     box9 = colorCoding(x1, y1+310, x2, y2+310, "Medium Sea Green", "field")
     box9.draw(win)
     box10 = colorCoding(x1, y1+345, x2, y2+345, "gainsboro", "parking lot")
     box10.draw(win)
     box11 = colorCoding(x1, y1+380, x2, y2+380, "Dodger Blue", "river")
     box11.draw(win)
     box12 = colorCoding(x1, y1+415, x2, y2+415, "Dim Gray", "road")
     box12.draw(win)
     box13 = colorCoding(x1, y1+450, x2, y2+450, "Dark Green", "tree")
     box13.draw(win)

def compass():
     #to draw a compass that appears on the upper left, used to help navigate directions

     #arrows
     t1 = Polygon(Point(50, 50), Point(42,50), Point(50, 25))
     t2 = Polygon(Point(50, 50), Point(58,50), Point(50, 25))
     t3 = Polygon(Point(50, 50), Point(50,42), Point(75, 50))
     t4 = Polygon(Point(50, 50), Point(50,58), Point(75, 50))
     t5 = Polygon(Point(50, 50), Point(42,50), Point(50, 75))
     t6 = Polygon(Point(50, 50), Point(58,50), Point(50, 75))
     t7 = Polygon(Point(50, 50), Point(50,42), Point(25, 50))
     t8 = Polygon(Point(50, 50), Point(50,58), Point(25, 50))
     
     t1.setFill("black")
     t2.setFill("grey")
     t3.setFill("black")
     t4.setFill("grey")
     t5.setFill("black")
     t6.setFill("grey")
     t7.setFill("black")
     t8.setFill("grey")
     t1.draw(win)
     t2.draw(win)
     t3.draw(win)
     t4.draw(win)
     t5.draw(win)
     t6.draw(win)
     t7.draw(win)
     t8.draw(win)

     textN = Text (Point(80,50),"N")
     textN.draw(win)
     textW = Text (Point(50,20),"W")
     textW.draw(win)
     textE = Text (Point(50,85),"E")
     textE.draw(win)
     textS = Text (Point(20,50),"S")
     textS.draw(win)
     c = Circle(Point(50, 50), 10)
     c.setFill("black")
     c.draw(win)
     
def combineInfo(items, dates):
     #get date-building csv file
     #get shared map csv file
     #remove any invalid lines
     #use date-building csv to assign building name with years so can be color coded accordingly

     yearList1 = []
     nameList1 = []
     for dateItem in dates:
          dateItem = (str(dateItem)).strip( ).split('\n')
          year = (str(dateItem))[2:6]
          nameList = (((str(dateItem))[7:-2]).lower().split(' '))
          name = str("".join(nameList))
          name1List = str(name).split(".")
          name = str("".join(name1List))
          nameList1.append(name)
          yearList1.append(year)

     nameList1 = nameList1
     yearList1 = yearList1
     
     #split up items from map csv
     #get rid of invalid lines, if necessary
     itemName = {} #dictionary
     countTree = 0
     for item in items:
          try:               
               item = item.split("\n")
               if (str(item)).find('#') != -1:#get rid of lines that have '#'
                    continue
               item = (str(item)).split(",")#get rid of lines that are too short
               if len(item) <= 5:
                    continue
               
               #used for specific lines that create more pleasing polygons
               if item[3:6] == [' McCulloch', 'Mockler', 'Strohbeck']:
                    item[3] = " and ".join(item[3:6])
                    item[4] = item[6]
                    name = name+"1"
                    item[0] = item[0]
                    item[2] = item[2]
                    item[5:-2] = item[7:-2]

               if item[3] == " Lynn Albright":
                    item[5:-2] = item[4:-2]
                    item[4] = "4"
               if item[4] == " Quadrant 4":
                    item[4] = item[4].replace(" Quadrant ", "")

               quadrant = (str(item[4]+"z")).strip()
               quadrantList = ["1z","2z","3z","4z"]
               
               if not quadrant in quadrantList:
                    continue         
               quadrant = quadrant.strip("z")
               
               #designating each variable
               category = ((item[0])[2:]).lower()#insignificant
               nameList2 = item[1].lower().split(' ')
               name = "".join(nameList2)
               colorList2 = item[2].lower().split(' ')
               color2 = "".join(colorList2)
               coordinate = item[5:-2]
               category = str(item[0])
               categoryList = str(category[2:len(category)]).lower().split(" ")
               category = "".join(categoryList)
               pairsList = item[3].lower().split(" ")
               pairs = "".join(pairsList)

               if name.find('/') != -1:#get rid of connected names (ex: wilson/morrow, etc)
                    continue
               if name.find('-') != -1:
                    if name == "sunnyside-childcarecenter" or name == "campusschool-gillhall" or name == "sabin-reedhall":
                         name = name
                    else:
                         continue

               #fixing specific issues in order to add more valid lines and get a better polygon possibly
               #also continuing to filter through specific lines that are better than the ones with the "better coordinates"
               if name.find("john") != -1:
                    name = "johnmgreenehall"
               if name.find("(") != -1:
                    if not (name.find("(cdo)") != -1):
                         continue
               if not color2 in colors: #get rid of colors that aren't colors such as names
                    continue
               if name == "chapinlawn":
                    if category == "lawn":
                         continue
               if name == "sabin-reedhall":
                    name = "sabinreedhall" 
               if category == "river":
                    if name == "paradiseroad":
                         continue
               if category == "building":
                    if name == "courts":
                         continue
               if name == "paradisepond":
                    if not pairs == "jocelynkofkeandarianameredith":
                         continue
               if pairs == "mccullochandmocklerandstrohbeck":
                    if name == "seelyelawn":
                         continue
               if pairs == "kalynnkosykaandjiyoungyun":
                    if name == "lymanconservatory":
                         continue
               if pairs == "kalynnkosykaandjiyoungyun":
                    if name in validHouses:
                         category = "house"

               lenCoor = len(coordinate)//2
               if category == "parkinglot":
                    if lenCoor < 3:
                         continue
               if name.find("greent") != -1:
                    name = name.replace("greent", "green")

               if pairs == "luciasimovaandhopemackeith":
                    coordinate1 = ", ".join(coordinate)
                    findExcessCommas = int(coordinate1.find(", , , , , ,"))
                    coordinate = (coordinate1[:findExcessCommas]).split(",")
                    if name == "elmstreet":
                         continue

               if category == "tree":
                    if name == "trees":
                         countTree += 1
                         name = name+str(countTree)
               if name.find("gym") != -1:
                    name = name.replace("gym", "gymnasium")
                        
               if category == "house" :
                    if not name.find("house") != -1:
                         name = name+"house"


                         #considering the mispelled houses such as martha wilson house vs wilson
                    if name.find("ducketthouse") != -1:
                         name = "eleanorducketthouse"
                         if not pairs == "kalynnkosykaandjiyoungyun":
                              continue
                    if name.find("chasehouse") != -1:
                         name = "maryellenchasehouse"
                         if not pairs == "kalynnkosykaandjiyoungyun":
                              continue
                    if name.find("emersonhouse") != -1:
                         name = "ellenemersonhouse"
                         if not pairs == "kalynnkosykaandjiyoungyun":
                              continue
                    if name.find("wilsonhouse") != -1:
                         name = "marthawilsonhouse"
                         if not pairs == "kalynnkosykaandjiyoungyun":
                              continue
                    if name.find("kinghouse") != -1:
                         name = "franklinkinghouse"
                         if not pairs == "kalynnkosykaandjiyoungyun":
                              continue
                    if name.find("scaleshouse") != -1:
                         name = "laurascaleshouse"
                         if not pairs == "kalynnkosykaandjiyoungyun":
                              continue
                    if name.find("president'shouse") != -1:
                         name = "presidentshouse"
                    if name == "friedmanapt.house":
                         name = "friedmancomplex"
                    if name.find("annex") != -1:
                         name = name.replace("house", "")

               if name.find("seelye") != -1 and not name.find("hall") != -1 and not name.find("lawn"):
                    name = name+"hall"
               #fixing specific typing like neilson to neilsonlibrary
               if name.find("neilson") != -1 and not name.find("library") != -1:
                    name = name+"library"    
               if name.find("ave") != -1 and not name.find(".") != -1 and not name.find("avenue") != -1:
                    name = name.replace("ave", "avenue")
               if name.find("ave.") != -1:
                    name = name.replace("ave.", "avenue")
               if name.find("bridge") != -1:
                    name = "lamont"+name
               if name == "comstockhouse" or name == "wilderhouse" or name == "gardinerhouse" or name == "jordanhouse" or name == "cushinghouse":
                    if not pairs == "kalynnkosykaandjiyoungyun":
                         continue
                    
               if category == "parking":
                    category = category.replace("parking", "parkinglot")                   
               if category == "parkinglot":
                    if pairs == "leighandnatalia":
                         if name == "p2" or name == "p3":
                              continue

               validBuildings = False
               if (name in validItems) == True:
                    if (category in validCategories) == True:
                         validBuildings = True

                         if (name in nameList1) == True:
                              index = nameList1.index(name)
                              yearItem = int(yearList1[index])
                              if yearItem <= 1750:
                                   color = "thistle"
                              if yearItem <= 1800:
                                   color = "purple"
                              elif yearItem <= 1850:
                                   color = "violet"
                              elif yearItem <= 1900:
                                   color = "darkviolet"
                              elif yearItem <= 1950:
                                   color = "mediumorchid"
                              elif yearItem <= 2000:
                                   color = "orchid"
                              else:
                                   if yearItem <= 2050:
                                        color = "mediumvioletred"

                         else:
                              category = category.strip()
                              #make everything that that does not have a year associated a faded color,
                              #so it doesn't attract away from the buildings with actual dates
                              if category == "field":
                                   name = name+"+"+category
                              elif category == "lawn":
                                   name = name+"+"+category
                              elif category == "parkinglot":
                                   name = name+"+"+category
                              elif category == "river":
                                   name = name+"+"+category
                              elif category == "road":
                                   name = name+"+"+category
                              elif category == "tree":
                                   name = name+"+"+category
                              else:
                                   if category == "building" or category == "house":
                                       name = name+"+"+category #red are the buildings/houses that do not have a year assigned, so unknown year

                    else:
                    
                         continue
               else:
                    continue

               if not validBuildings: continue
          
               if name not in itemName.keys():
                    itemName[name] = coordinate
               else:
                    if len(coordinate) > len(itemName[name]):
                         itemName[name] = coordinate

                    else:
                         continue

          except:
               continue

     for key, value in itemName.items():
          #loop through the keys in the itemName dictionary in order to look at the "chosen" lines
          try:
               polygon = []
               name = key
               coordinate = value
               for x, y in zip(range(0, len(coordinate), 2), range(1, len(coordinate), 2)): #alternate the numbers so every even is x and every odd is y
                    X = coordinate[x].strip() #removing any excess un-needed info
                    Y = coordinate[y].strip() #removing any excess un-needed info
                    points = Point(X, Y) #creating point
                    polygon.append(points)#add point to polygon

               if not (name in nameList1) == True:
                    if name.find("+") != -1:
                         indexNum = int(name.find("+"))
                         category = name[indexNum+1:len(name)]
                         name = name[:indexNum]
                         #color code by category
                         if category == "field" or category == "lawn":
                              color = "Medium Sea Green"
                         elif category == "parkinglot":
                              color = "gainsboro"
                         elif category == "river":
                              color = "Dodger Blue" 
                         elif category == "road":
                              color = "Dim Gray"
                         elif category == "tree":
                              color = "Dark Green"
                         else:
                              if category == "building" or category == "house":
                                   color = "red"
               else:
                    #color code according to date if it has a date
                    index = nameList1.index(name)
                    yearItem = int(yearList1[index])
                    validBuildings = True
                    if yearItem <= 1750:
                         color = "thistle"
                    if yearItem <= 1800:
                         color = "purple"
                    elif yearItem <= 1850:
                         color = "violet"
                    elif yearItem <= 1900:
                         color = "darkviolet"
                    elif yearItem <= 1950:
                         color = "mediumorchid"
                    elif yearItem <= 2000:
                         color = "orchid"
                    else:
                         if yearItem <= 2050:
                              color = "mediumvioletred"

               createMap(name, color, polygon)
               
          except:
               continue
          
def createMap(name, color, polygon):
     #to create the map of each item/polygon and color coding

     poly = Polygon(polygon) #objectifying the polygon
     poly.draw(win) #draw on window
     poly.setFill(color)#fill in color based on that house

def openSmithMapCSV(file):
     #to open the smith map csv that is has been collaborated by every csc111 student
     file = open(file, "r")
     lines = file.readlines()
     file.close()
     return lines
          
def openDatesCSV(file):
     #to open the date-building file that has described the year the building has been constructed
     file = open(file, "r")
     lines = file.readlines()
     file.close()
     return lines


#############################################################################
#
#                                 MAIN
#
#############################################################################

def main():
     #open Smith Map Group CSV file with a different function
     mapInfo = openSmithMapCSV(MapCSV)
     win.setBackground("Dark Sea Green") #background, to make a more realistic map
     
     #open Smith Building Construction dates with a different function
     dates = openDatesCSV(DatesCSV)
     
     #compare both information in another function
     #which then calls a function, createMap, in order to draw out the map
     combineInfo(mapInfo, dates)
     
     #display compass
     #display legend
     lengend()
     compass()
     
main()

