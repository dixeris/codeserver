import sys
import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:5556")

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
#이 소스코드 실행 커맨드 뒤에 나오는 숫자가 zip code, 숫자가 지정되지 않은 경우는 10001 
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

total_temp = 0
for update_nbr in range(20):
    string = socket.recv_string()
    zipcode, temperature, relhubidity = string.split()
    total_temp     += int(temperature)
    print(f"Recive temper for zipcode"
    f"'{zip_filter}' was {temperature} F")

print((f"Avg temp for zipcode"
f"'{zip_filter}' was {total_temp} / {update_nbr+1} F"))


