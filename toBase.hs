--Klutix
--Accepts n and a base and converts n to base equivalent. Works up to base 62
toBase::Int->Int->String
toBase v b
   | v > 0 = toBase (v`div`b) b ++ ["0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"!!(v `mod` b)]
   | otherwise = ""
