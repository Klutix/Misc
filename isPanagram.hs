isPanagram::String->Bool
isPanagram str = do
    let lower = map toLower str
    all(==True) $ map(\x-> x `elem` lower) "abcdedghijklmnopqrstubwxyz"

main = putStrLn $ show $ isPanagram "The Quick brown fox jumps over the lazy dog"
