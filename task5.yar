rule wannacry{

    strings:

        $string1 = "msg/m_bulgarian.wnry"

        $string2 = "msg/m_chinese (simplified).wnry"

        $string3 = "msg/m_chinese (traditional).wnry"

        $string4 = "msg/m_croatian.wnry"

        $string5 = "msg/m_czech.wnry"

        $string6 = "msg/m_danish.wnry"

        $string7 = "msg/m_dutch.wnry"

        $string8 = "msg/m_english.wnry"

        $string9 = "msg/m_filipino.wnry"

        $string10 = "msg/m_finnish.wnry"

        $string11 = "msg/m_french.wnry"

        $string12 = "msg/m_german.wnry"

        $string13 = "msg/m_greek.wnry"

        $string14 = "msg/m_indonesian.wnry"

        $string15 = "msg/m_italian.wnry"

        $string16 = "msg/m_japanese.wnry"

        $string17 = "msg/m_korean.wnry"

        $string18 = "msg/m_latvian.wnry"

        $string19 = "msg/m_norwegian.wnry"

        $string20 = "msg/m_polish.wnry"

        $string21 = "msg/m_portuguese.wnry"

        $string22 = "msg/m_romanian.wnry"

        $string23 = "msg/m_russian.wnry"

        $string24 = "msg/m_slovak.wnry"

        $string25 = "msg/m_spanish.wnry"

        $string26 = "msg/m_swedish.wnry"

        $string27 = "msg/m_turkish.wnry"

        $string28 = "msg/m_vietnamese.wnry"

        $string29 = "Ooops, your files have been encrypted!"

        $string30 = "Wanna Decryptor"

        $string31 = ".wcry"

        $string32 = "WANNACRY"

        $string33 = "WANACRY!"

        $string34 = "icacls . /grant Everyone:F /T /C /Q"

        $string35 = "USERIDPLACEHOLDER@"

        $string36 = "TREEIDPLACEHOLDER"

        $string37 = "LANMAN1.0"

        $string38 = "LANMAN2.1"  

        $string41 = "TREEPATH_REPLACE"

        $string42 = "/KUSERIDPLACEHOLDER__"  

    condition:

        any of ($string*)

}
