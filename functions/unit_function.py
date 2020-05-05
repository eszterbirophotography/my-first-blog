def inches_to_cm(inches):
    return float(inches) * 2.54

def convert_inches(input_msg, result_msg, warning_msg):
    try:
        inches = input(input_msg)
        cm = inches_to_cm(inches)
        message = result_msg.format(inches, cm)
        print(message)

    except:
        ValueError
        warning = warning_msg
        print(warning)
