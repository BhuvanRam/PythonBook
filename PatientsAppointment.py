from ConsultQueue import ConsultQueue
from PatientRecord import PatientRecord

class PatientAppointment:
    index = 1001
    consultQueue = ConsultQueue()
    newPatients = []
    priorityQueuePatients = []
    FirstFile = 0

    def BookAppointments(self):
        self.readPatientsData("inputPS5a.txt")
        self.writePatientsData()

        self.FirstFile = 1
        self.readPatientsData("inputPS5b.txt")

    # Reads the Patients data from  inputPS5a.txt file
    def readPatientsData(self, fileName):
        patientsFile = open(fileName, "r")
        patientsData = patientsFile.readlines()

        for patient in patientsData:
            if "newPatient" in patient:
                patientDetails = patient.split(",")
                patientDetails[0] = patientDetails[0].replace("newPatient:", " ").strip()
            elif "nextPatient" in patient:
                self.nextPatient()
            else:
                patientDetails = patient.split(",")

            if "nextPatient" not in patient:
                registeredPatient = self.registerPatient(patientDetails[0], int(patientDetails[1]))
                self.enqueuePatient(registeredPatient)

            if "newPatient" in patient:
                self.writeNewPatientData(registeredPatient)
                self.writePatientsData()

    # Assigns patientId
    def registerPatient(self, name, age):
        patient = PatientRecord(name, age, self.index)
        self.index += 1
        return patient

    def enqueuePatient(self, patient):
        self.consultQueue.addPatientsToQueue(patient)

    def dequeuePatient(self):
        self.consultQueue.dequeue()

    def nextPatient(self):
        # Creates the file if not there and clears the file
        self.priorityQueuePatients = self.consultQueue.returnConsultQueue()
        patientsOutputFile = open("outputPS5.txt", "a+")
        patientsOutputFile.write("----Next Patient----\n")

        # As per the Heap Binary Tree Formulae , the first index element is the root node
        # So appending top index element to file
        output = "Next Patient for consultation is: " + self.priorityQueuePatients[0].PatId + "," \
                 + self.priorityQueuePatients[0].name + "\n"
        patientsOutputFile.write(output)

        patientsOutputFile.write("---------------------\n")
        patientsOutputFile.close()

        # Dequeue patient from ConsultQueue
        self.dequeuePatient()

    # Write the Patients data to outputPS5.txt file
    def writePatientsData(self):
        # Creates the file if not there and clears the file
        patients = self.consultQueue.returnConsultQueue() # Lever Order Heap
        patients = self.consultQueue.getPatientsList(patients) #Sorted Order

        patientsOutputFile = open("outputPS5.txt", "a+")

        if self.FirstFile == 0:
            patientsOutputFile.truncate(0)
            patientsOutputFile.write("---- Initial Queue ----\n")
            patientsOutputFile.write("No of Patients added : " + str(len(patients)) + "\n")

        patientsOutputFile.write("Refreshed Queue : \n")
        for patient in patients:
            patientsOutputFile.write(patient.PatId + "," + patient.name + "\n")
        patientsOutputFile.write("---------------------\n")

        patientsOutputFile.close()

    def writeNewPatientData(self, patient):
        patientsOutputFile = open("outputPS5.txt", "a+")
        patientsOutputFile.write("--- New Patient Entered ---- \n")
        patientsOutputFile.write(
            "Patient details : " + patient.name + "," + str(patient.age) + "," + patient.PatId + "\n")
        patientsOutputFile.close()

    # Print the patients data
    def printPatients(self, priorityQueuePatients):
        for patient in priorityQueuePatients:
            print(str(patient.PatId) + " " + str(patient.name) + " " + str(patient.age))

def main():
    patientAppointment = PatientAppointment()
    patientAppointment.BookAppointments()

if __name__ == '__main__':
    main()