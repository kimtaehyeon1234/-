import pickle
import os

filepath= "score.bin"
def save_data(score, avg):
    with open(filepath, "wb") as file:
        pickle.dump(score, file)
        pickle.dump(avg, file)
        

def load_data():
    with open(filepath, "rb") as file:
        score= pickle.load(file)
        avg= pickle.load(file)  

    return score, avg

def input_scores():
    score= []
    i=1
    while True:
        a=int(input(f"#{i}? "))
        i+=1
        if a<0:
            break
        score.append(a)
    return score

def get_average(s):
    total=0
    for a in s:
        total+=a
    return total/len(s)

def show_scores(s):
    for a in s:
        print(a,end=" ")
    print()
        
if os.path.exists(filepath):
    n_score, n_avg= load_data()
    print("[파일 읽기]\n\n[점수 출력]")
    print("개인점수:",end=" ")
    show_scores(n_score)
    print(f"평균: {n_avg:.1f}")
else:
    print("[점수 입력]")
    score= input_scores()
    print("\n[점수 출력]")
    print("개인점수:",end=" ")
    show_scores(score)
    avg=get_average(score)
    print(f"평균: {avg:.1f}")
    save_data(score, avg)






