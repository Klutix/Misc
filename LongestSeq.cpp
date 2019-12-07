string longestSeq(string str1, string str2, string longest = ""){
    if (str1.size() > str2.size())
        swap(str1,str2);
    for(int st1 = 0;st1 < str1.size();st1++)
        for (int st2 = 0; st2 < str1.size(); st2++)
            for (int end1 = 1; end1 < str1.size(); end1++)
                for (int end2 = 1; end2 < str2.size(); end2++)
                    if (str1.substr(st1, end1) == str2.substr(st2, end2))
                        if (longest.size() < str2.substr(st2, end2).size())
                            longest = str2.substr(st2, end2);
    return longest;
}
