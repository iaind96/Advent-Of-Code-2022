
def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip() for line in file]
    return lines


def ProcessStream(stream, packetLength):
    streamIndex = packetLength
    while streamIndex <= len(stream):
        currentChunk = stream[(streamIndex-packetLength):streamIndex]
        if len(set(currentChunk)) == len(currentChunk):
            break
        streamIndex += 1

    print(f'Total characters processed = {streamIndex}')


if __name__ == '__main__':

    # streams = ReadInput(r'inputs\day6_example.txt')
    streams = ReadInput(r'inputs\day6.txt')

    ProcessStream(streams[0], 14)