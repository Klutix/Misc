--Klutix
--Accepts n and a base and converts n to base equivalent. Works up to base 62
toBase::Int->Int->String
toBase v b
   | v > 0 = toBase (v`div`b) b ++ ["0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"!!(v `mod` b)]
   | otherwise = ""
This paste expires on 2019-08-28 04:38:32. View raw. Remove now. Pasted through web.

View source code, the removal or expiry stories, or read the about page.
