# '''
#     This file contains the class definition for the StrawHat class.
# '''

# import crewmate
# import heap
# import treasure

# class StrawHatTreasury:
#     '''
#     Class to implement the StrawHat Crew Treasury
#     '''
    
#     def __init__(self, m):
#         '''
#         Arguments:
#             m : int : Number of Crew Mates (positive integer)
#         Returns:
#             None
#         Description:
#             Initializes the StrawHat
#         Time Complexity:
#             O(m)
#         '''
        
#         # Write your code here
#         pass
    
#     def add_treasure(self, treasure):
#         '''
#         Arguments:
#             treasure : Treasure : The treasure to be added to the treasury
#         Returns:
#             None
#         Description:
#             Adds the treasure to the treasury
#         Time Complexity:
#             O(log(m) + log(n)) where
#                 m : Number of Crew Mates
#                 n : Number of Treasures
#         '''
        
#         # Write your code here
#         pass
    
#     def get_completion_time(self):
#         '''
#         Arguments:
#             None
#         Returns:
#             List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
#         Description:
#             Returns all the treasure after processing them
#         Time Complexity:
#             O(n(log(m) + log(n))) where
#                 m : Number of Crew Mates
#                 n : Number of Treasures
#         '''
        
#         # Write your code here
#         pass
    
#     # You can add more methods if required


    
'''
    This file contains the class definition for the StrawHat class.
'''

# import crewmate
# import heap
# import treasure
from crewmate import CrewMate
from heap import Heap,min_comparision_crewmate,min_comparison,id_comparator
from treasure import Treasure


class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''

        
        self.crew_heap= Heap(min_comparision_crewmate,[])
        for i in range(m):
            b=CrewMate()
            self.crew_heap.insert(b)
        self.arrival_time=[]
        self.completion_time_list=[]
        self.global_treasures=[]
        self.all_crewmates_list=[]
        self.arrival_time_list=[]
        # Write your code here
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        self.arrival_time_list.append(treasure.arrival_time)
        min_load_crewmate=self.crew_heap.extract()

        if min_load_crewmate.assigned==False:
            self.all_crewmates_list.append(min_load_crewmate)
            min_load_crewmate.assigned=True
        
        if min_load_crewmate.load<=treasure.arrival_time:
            min_load_crewmate.load = treasure.size+treasure.arrival_time
        else:
            min_load_crewmate.load+=treasure.size
        min_load_crewmate.treasure_heap.append([treasure.remaining_size+treasure.arrival_time,treasure.id,treasure.size,treasure.arrival_time,treasure.remaining_size])        # [treasure.id,treasure.size,treasure.arrival_time]

        self.crew_heap.insert(min_load_crewmate)

        pass

    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        completion_list = []
        treasure_completed_during_process=[]
        for crewmate in self.all_crewmates_list:

            new_heap=Heap(min_comparison,[])

            crew_completion_time=[] 
            # reset = 0
            for idx,tres in enumerate(crewmate.treasure_heap):
                arrival_time = tres[3]
                remaining_size_of_tres=tres[4]
                treasure_id=tres[1]
                size=tres[2]
                curr_time=arrival_time
                new_treasure=Treasure(treasure_id,size,arrival_time)
                new_treasure.remaining_size=tres[4]
                new_comp_time=new_treasure.remaining_size+new_treasure.arrival_time
                new_heap.insert([new_comp_time,new_treasure.id,new_treasure.size,new_treasure.arrival_time,new_treasure.remaining_size,new_treasure.completion_time])

                if idx+1<len(crewmate.treasure_heap):
                    next_tres=crewmate.treasure_heap[idx+1]
                    p_time=next_tres[3]-arrival_time
                    while not new_heap.isempty() and p_time!=0:
                        curr_tres=new_heap.extract()
                        if curr_tres[4]<p_time:
                            p_time=p_time-curr_tres[4]
                            # completed_treasure=new_heap.extract()
                            # completed_treasure[4]=0
                            # curr_tres[0]=curr_tres[4]+arrival_time
                            curr_tres[5]=curr_tres[4]+curr_time
                            temp_tres=Treasure(curr_tres[1],curr_tres[2],curr_tres[3])
                            temp_tres.completion_time=curr_tres[5]
                            temp_tres.remaining_size=curr_tres[4]
                            treasure_completed_during_process.append(temp_tres)
                            curr_time+=curr_tres[4]

                        else:
                            curr_tres[4]=curr_tres[4]-p_time
                            p_time=0
                            curr_tres[0]=curr_tres[4]+arrival_time
                            new_heap.insert([curr_tres[0],curr_tres[1],curr_tres[2],curr_tres[3],curr_tres[4],curr_tres[5]])
    
            while not new_heap.isempty():

                last_tres=new_heap.extract()
                last_tres[5]+=curr_time+last_tres[4]
                curr_time+=last_tres[4]
                temp_tres=Treasure(last_tres[1],last_tres[2],last_tres[3])
                temp_tres.completion_time=last_tres[5]
                temp_tres.remaining_size=last_tres[4]

                crew_completion_time.append(temp_tres)         
            completion_list+=crew_completion_time

        completion_list+=treasure_completed_during_process
        sorted_ans=sorted(completion_list,key=lambda x: x.id)

        return sorted_ans

        pass

    # You can add more methods if required



    