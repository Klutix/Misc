split::String->Char->[String]->[String]
split [] _ _= [[]]
split [x] _ _ = [[x]]
split (x:xs) _ [[]] = [(x:xs)]
split (x:xs) delim base = solution
  where
    tuple = break (==delim) (x:xs)
    tuplength = (length (snd tuple)) 
    v1 = fst $ tuple 
    mystr
      | tuplength > 0 = tail $ snd tuple 
      | otherwise = fst tuple
    solution
      | tuplength > 0 = base++split mystr delim ([v1]) 
      | otherwise = base++split mystr delim [[]]
