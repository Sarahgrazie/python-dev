import multiprocessing

def calc(a,b,c):
    return a * b + c      # 상승률 증가율 멀티 프로세싱으로 :계산하는 코드

input_list = [(1,2,3,),(4,5,6,),(7,8,9,),(10,11,12)]

#process pool 프로세스를 먼저 생성 
pool = multiprocessing.Pool(processes=4)

#병렬처리를 위한 map 메소드 정의
output_list =pool.starmap(calc, input_list)

#프로세스 풀 종료 
pool.close()
pool.join()   #모든 process가 종료될 때 까지 대기를 시키는 것 

print(output_list)