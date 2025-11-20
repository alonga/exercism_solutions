"""Functions to prevent a nuclear meltdown."""


"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    efficiency = voltage * current / theoretical_max_power * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    generated_power = temperature * neutrons_produced_per_second
    efficiency_percent = generated_power / threshold * 100

    if efficiency_percent < 90:
        return "LOW"
    elif 90 <= efficiency_percent <= 110:
        return "NORMAL"
    else:
        return "DANGER"

    

   
