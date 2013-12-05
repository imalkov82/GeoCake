################################################
################################################
#   _____             _____      _ 
# / ____|           / ____|     | |       
# | |  __  ___  ___ | |    __ _ | | _____
# | | |_ |/ _ \/ _ \| |   /  _` | |/ / _ \
# | |__| |  __/ (_) | |___| (_| |   <  __/
# \_____|\___|\___/ \_____\__,_|_|\_\___|
#################################################
#################################################

from difflib import SequenceMatcher

class Group:
    #constructor
    def __init__(self, arr_corelog=None):
        pass
        
    #methods
    def add_corelog(corelog_object):
        pass
    def remove_corelog(corelog_tag):
        pass
    def _buildUnMachedSq(m_sq):
        pass
    def combineCLByGeometry(cl1_tag, cl2_tag):
        s = SequenceMatcher(None, cl1_tag, cl2_tag)
        mached_blocks = s.get_matching_blocks()
        unmchd_sq = []
        index = 0
        while index < len(mached_blocks)-1:
            unmchd_sq[index] =  cl1_tag[mached_blocks[index][0]+mached_blocks[index][2]:mached_blocks[index+1][0]]
            unmchd_sq[index].append = cl2_tag[mached_blocks[index][1]+mached_blocks[index][2]:mached_blocks[index+1][1]]
            
    def unite_corelogs(cl1_tag, cl2_tag):
        pass
        

            
            
