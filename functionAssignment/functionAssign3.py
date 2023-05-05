def justify(list1, sz):
    n = len(list1)

    if 2*n - 1 > sz or list1 == [] or len(list1) == 1:
        return " ".join(list1)
    
    char = 0

    for word in list1:
        char += len(word)
    
    avg = (sz - char) // (len(list1) - 1)

    rem = sz - char - avg * (len(list1) - 1)

    sent = ""

    for i in range(len(list1)):
        sent += list1[i]
        sent += " " * avg

        if rem > 0:
            sent += " "
            rem -= 1
    

    return sent


story = [
"Vincent Massey Secondary School has again",
"received top marks from the Fraser Institute.",
"The national think-tank, which provides annual",
"test scores for schools across Ontario,",
"released its findings this month.",
"",
"Most schools in Windsor-Essex showed improvement,",
"but Massey scored highest locally with 8.2 out of",
"10 to finish 50th out of 740 schools in the province.",
"",
"St. Anne Catholic High School in Lakeshore was the",
"second place local finisher for the 2015-2016 year",
"with a score of 8.1 and earning 57th place.",
""
"Schools are scored based on seven academic indicators",
"found in the results of annual math and literacy",
"tests.",
"",
"When the institute released its report on elementary",
"schools in December, Bellewood Public School scored",
"top marks for the area with a 9.3 — good enough for",
"35th place out of 2,900 schools across the province."]

for line in story:
    print("|",justify(line.split(),56),"|")