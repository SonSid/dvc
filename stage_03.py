with open("artifact.txt","r") as f:
    text=f.read()

with open("artifact.txt","w") as f:
    text=f.write(text+"I have maded the change")


print(text)
print("Its the End of Stage 03")