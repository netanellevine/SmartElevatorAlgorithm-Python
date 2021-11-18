class Calls:

    def __init__(self, calls):
        self.calls = calls
        self.length = len(self.calls)

    def add_more_then_one(self, curr_call, elevator):
        call_time = curr_call.runTime
        call_src = curr_call.src
        call_dest = curr_call.dest
        call_type = 1 if call_src < call_dest else -1
        call_ind = curr_call.call_ind
        amount_calls_to_add = 0
        for i in range(call_ind + 1, len(self.calls)):
            c = self.calls[i]
            time_between_calls = c.runTime - call_time
            if time_between_calls > 5.0:
                break
            elif call_type == 1 and call_src < c.src:
                if elevator.get_distance(call_src, c.src) > time_between_calls:
                    amount_calls_to_add += 1
            elif call_type == -1 and call_src > c.src:
                if elevator.get_distance(call_src, c.src) > time_between_calls:
                    amount_calls_to_add += 1
        return amount_calls_to_add
