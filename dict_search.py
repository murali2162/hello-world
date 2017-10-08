st=input("Enter a word or sentence. Make sure it's large enough to search:  ")
let=input("Enter a letter to search:  ")
if let in st:
    print("letter found and repeated",st.count(let),"times")
    st=st[::-1]
    print("reversed string is:", st)
    
else:
    print("letter not found")