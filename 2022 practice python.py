class Enemy:
# the emeny ojects are what the player fights in the game #
    def __init__(self, name, health ):
        #the init function is called when a new object is instantiated, it begins and ends with two underscores 
    # set the name 
        self._name = name
        #set the health
        self._health = health  
        # Append the new enemy into the enemy_list
        enemy_list.append(self)        
        # scare the world
        print("mwh ahahhhahahahah")
        
    def get_name(self):
        ''' this function returns the name of the enemy object '''
    
        return self._name
    
    def get_health(self):
        ''' This is a getter function that returns the health of the enemy '''
    
        return self._health
    
    
# create a list to store all enemy objects 
enemy_list = []
# create new enemy object 
Enemy("Gru", 15)
Enemy("Vlad the Impaler", 3)

def attacked(self, damage):
        
    self._health -= damage
    if self._health <= 0:
        print(f"{self._name} is dead")
    else:
        print(f"Ouch, {self._name} is hurt")   
        
def display_enemies():
    ''' This function loops through the enemy_list and displays their names and health '''
        
    for e in enemy_list:
        print(f"{e.get_name()} has {e.get_health()} health")
        
display_enemies()

