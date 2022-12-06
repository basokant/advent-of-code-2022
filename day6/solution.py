test = "bvwbjplbgvbhsrlpgdmjqwftvncz"

f = open("./input.txt", 'r')
input = f.readline()

def find_start_of_packet(signal: str) -> int:
    current_packet_set = set()
    signal = list(signal)

    l, r = 0, 0
    while (r < len(signal)):
        LENGTH_OF_PACKET = 4
        start_char = signal[l]
        last_char = signal[r]

        if ((l - r + 1) <= LENGTH_OF_PACKET) :
            if (last_char not in current_packet_set) :
                current_packet_set.add(last_char)
                if (len(current_packet_set) == LENGTH_OF_PACKET) :
                    return l
                r += 1
            else :
                current_packet_set.remove(start_char)
                l += 1
    
print(find_start_of_packet(test) + 4)
print(find_start_of_packet(input) + 4)

def find_start_of_message(signal: str) -> int:
    current_message_set = set()

    signal = list(signal)

    l, r = 0, 0
    while (r < len(signal)):
        LENGTH_OF_MESSAGE = 14
        start_char = signal[l]
        last_char = signal[r]

        if ((l - r + 1) <= LENGTH_OF_MESSAGE) :
            if (last_char not in current_message_set) :
                current_message_set.add(last_char)
                if (len(current_message_set) == LENGTH_OF_MESSAGE) :
                    return l
                r += 1
            else :
                current_message_set.remove(start_char)
                l += 1

print(find_start_of_message(test) + 14)
print(find_start_of_message(input) + 14)