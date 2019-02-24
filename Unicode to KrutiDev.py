
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[2]:


def ReplaceFirstOccurrence(Source,Find,Replace):
    Place = Source.find(Find)
    startP = Source[:Place]
    endP = Source[Place+len(Find):]
    newStr = startP + Replace + endP
    return newStr


# In[3]:


class UnicodeToKrutidev:
    
    def __init__(self):
    
        self.array_one = ["‘",   "’",   "“",   "”",   "(",    ")",   "{",    "}",
                 "=", "।",  "?",  "-",  "µ", "॰", ",", ".", "् ","०",  "१",
                 "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९", "x",
                 "फ़्",  "क़",  "ख़",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",
                 "ऱ",  "ऩ", "त्त्",   "त्त",     "क्त",  "दृ",  "कृ","ह्न",  "ह्य",  "हृ",
                 "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष्", "क्ष", "त्र्", "त्र","ज्ञ", "छ्य",  "ट्य",
                 "ठ्य",  "ड्य",  "ढ्य", "द्य","द्व", "श्र",  "ट्र",    "ड्र",    "ढ्र", "छ्र",
                 "क्र",  "फ्र",  "द्र",   "प्र",   "ग्र", "रु",  "रू", "्र","ओ",  "औ",
                 "आ",   "अ",   "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ", "क्",
                 "क",  "क्क",  "ख्",   "ख",    "ग्",   "ग",  "घ्",  "घ",    "ङ",
                 "चै",   "च्",   "च",   "छ",  "ज्", "ज",   "झ्",  "झ",   "ञ", "ट्ट",
                 "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड",   "ढ",  "ण्", "ण",
                 "त्",  "त",  "थ्", "थ",  "द्ध",  "द", "ध्", "ध",  "न्",  "न", "प्",
                 "प",  "फ्", "फ",  "ब्",  "ब", "भ्",  "भ",  "म्",  "म", "य्",  "य",
                 "र",  "ल्", "ल",  "ळ",  "व्",  "व", "श्", "श",  "ष्", "ष",  "स्",
                 "स",   "ह", "ऑ",   "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",
                 "ू",   "ृ",   "े",   "ै","ं",   "ँ",   "ः",   "ॅ",    "ऽ",  "् ", "्" ]

        self.array_two = ["^", "*",  "Þ", "ß", "¼", "½", "¿", "À", "¾", "A", "\\", "&",
                 "&", "Œ", "]","-","~ ", "å",  "ƒ",  "„",   "…",   "†",   "‡",
                 "ˆ",   "‰",   "Š",   "‹","Û", "¶",   "d",    "[k",  "x",  "T",
                 "t",   "M+", "<+", "Q",  ";",    "j",   "u", "Ù",   "Ùk", "Dr",
                 "–",   "—", "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{",
                 "{k",  "«", "=","K", "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|","}",
                 "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý",   "æ", "ç", "xz",
                 "#", ":","z","vks",  "vkS",  "vk",    "v",   "bZ",  "b",  "m",  "Å",
                 ",s",  ",",   "_", "D",  "d",    "ô",     "[",     "[k",    "X",   "x",
                 "?",    "?k",   "³", "pkS",  "P",    "p",  "N",   "T",    "t",
                 "÷",  ">",   "¥", "ê",      "ë",      "V",  "B",   "ì",       "ï", "M",
                 "<",  ".", ".k",   "R",  "r",   "F", "Fk",  ")",    "n", "/",  "/k",
                 "U", "u",   "I",  "i",   "¶", "Q",   "C",  "c",  "H",  "Hk", "E",
                 "e", "¸",   ";",    "j",  "Y",   "y",  "G",  "O",  "o", "'", "'k",
                 "\"", "\"k", "L",   "l",   "g", "v‚",    "‚",    "ks",   "kS",   "k",
                 "h",    "q",   "w",   "`",    "s",    "S","a",    "¡",    "%",     "W",
                 "·",   "~ ", "~"]

    
    def unicodeToKrutiDev(self,unicode_substring):
        array_one_length = len(self.array_one)
        modified_substring = unicode_substring

        position_of_quote = modified_substring.find("'")

        while position_of_quote >= 0 : 
            modified_substring =  ReplaceFirstOccurrence(modified_substring,"'","^")
            modified_substring =  ReplaceFirstOccurrence(modified_substring,"'","*")
            position_of_quote = modified_substring.find("'")

        position_of_Dquote = modified_substring.find("\"")

        while position_of_Dquote >= 0: 
            modified_substring =  ReplaceFirstOccurrence(modified_substring,"\"","ß")
            modified_substring =  ReplaceFirstOccurrence(modified_substring,"\"","Þ")
            position_of_Dquote = modified_substring.IndexOf("\"")


        modified_substring = modified_substring.replace( "क़", "क़" ) 
        modified_substring = modified_substring.replace( "ख़", "ख़" )
        modified_substring = modified_substring.replace( "ग़", "ग़" )
        modified_substring = modified_substring.replace( "ज़", "ज़" )
        modified_substring = modified_substring.replace( "ड़", "ड़" )
        modified_substring = modified_substring.replace( "ढ़", "ढ़" )
        modified_substring = modified_substring.replace( "ऩ", "ऩ" )
        modified_substring = modified_substring.replace( "फ़", "फ़" )
        modified_substring = modified_substring.replace( "य़", "य़" )
        modified_substring = modified_substring.replace( "ऱ", "ऱ" )


        position_of_f = modified_substring.find( "ि" ) 

        while ( position_of_f != -1 ):
            character_left_to_f = modified_substring[position_of_f - 1]
            modified_substring = modified_substring.replace( character_left_to_f + "ि" ,  "f" + character_left_to_f )
            position_of_f = position_of_f - 1

            while (( position_of_f != 0  ) and ( modified_substring[position_of_f - 1] == '्' ) ):
                string_to_be_Replaced = modified_substring[position_of_f - 2 ] + "्"
                modified_substring = modified_substring.replace( string_to_be_Replaced + "f", "f" + string_to_be_Replaced )
                position_of_f = position_of_f - 2

            position_of_f = modified_substring.find("ि", position_of_f + 1 ) # search for f ahead of the current position.



                #************************************************************     
                #     modified_substring = modified_substring.Replace( /fर्", "£"  )  ;
                #************************************************************     
                # Eliminating "र्" and putting  Z  at proper position for this.

        set_of_matras = "ािीुूृेैोौं:ँॅ"

        modified_substring += "  "  # add two spaces after the string to avoid UNDEFINED char in the following code.

        position_of_half_R = modified_substring.find( "र्" ) 
        while ( position_of_half_R > 0  ):  # while-04

            # "र्"  is two bytes long
            probable_position_of_Z = position_of_half_R + 2     
            character_right_to_probable_position_of_Z = modified_substring[probable_position_of_Z + 1]

            # trying to find non-maatra position right to probable_position_of_Z .

            while ( set_of_matras.find( character_right_to_probable_position_of_Z ) != -1 ):  

                probable_position_of_Z = probable_position_of_Z + 1 
                character_right_to_probable_position_of_Z = modified_substring[probable_position_of_Z + 1]
                #end of while-05

            string_to_be_Replaced = modified_substring[position_of_half_R + 2 : probable_position_of_Z - position_of_half_R - 1]  
            modified_substring = modified_substring.replace( "र्" + string_to_be_Replaced  ,  string_to_be_Replaced + "Z" )
            position_of_half_R = modified_substring.find( "र्" )
            # end of while-04

        modified_substring = modified_substring[0: len(modified_substring) - 2]

        for input_symbol_idx in range(array_one_length):

            idx = 0  #;  // index of the symbol being searched for Replacement

            while (idx != -1 ): #//whie-00
                modified_substring = modified_substring.replace(self.array_one [input_symbol_idx], self.array_two [input_symbol_idx])
                idx = modified_substring.find(self.array_one[input_symbol_idx])
                # end of while-00 loop
                #} // end of for loop


        return modified_substring;


# In[4]:


un = UnicodeToKrutidev()


# In[5]:


un.unicodeToKrutiDev("हिन्दी विकिपीडिया, विकिपीडिया का हिन्दी भाषा का संस्करण है, जिसका स्वामित्व विकिमीडिया संस्थापन के पास है।")

