from prescription_data import *

trail_patients = ['Denise', 'Eddie', 'Frank','Georgia','Kenny']
# for patient in trail_patients:
#     prescriptions = patients[patient]
#     prescriptions.remove(warfarin)
#     prescriptions.add(edoxaban)
#     print(patient,prescriptions)

# for patient in trail_patients:
#     prescriptions = patients[patient]
#     if warfarin in prescriptions:
#         prescriptions.remove(warfarin)
#         prescriptions.add(edoxaban)
#     else:
#
#         print(f"The patient {patient} didn't using warfarin.\n Please remove from the trail ")
#     print(patient, prescriptions)

### Because of above process it slow down the process so we are using try exception

for patient in trail_patients:
    prescriptions = patients[patient]
    try:
        prescriptions.remove(warfarin)
        prescriptions.add(edoxaban)
    except KeyError:

        print(f"The patient {patient} didn't using warfarin.\n Please remove from the trail ")
    print(patient, prescriptions)