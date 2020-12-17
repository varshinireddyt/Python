def maxEvents(arrival, duration):
    events = [0]
    sorted_arr, sorted_dur = zip(*sorted(zip(arrival,duration)))
    for i in range(len(arrival)-1):
        if sorted_arr[events[-1]]+sorted_dur[events[-1]] <= sorted_arr[i+1]:
            events.append(i+1)
        elif sorted_arr[events[-1]]+sorted_dur[events[-1]] >= sorted_arr[i+1]+sorted_dur[i+1]:
            events.pop()
            events.append(i+1)
    return len(events)