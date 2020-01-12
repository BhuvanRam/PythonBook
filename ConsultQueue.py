from PatientRecord import PatientRecord

class ConsultQueue:
    patients = []

    # Adding patients to queue
    def addPatientsToQueue(self, patient: PatientRecord):
        self.patients.append(patient)
        inputLength = len(self.patients) - 1

        # Performing Heapify O(n)
        while inputLength >= 0:
            self.patients = self.heapify(inputLength, self.patients)
            inputLength -= 1

    # Returns the queue in Level Order of Heap
        def returnConsultQueue(self):
        return self.patients

    # Returns the patients list in sorted order by age
    def getPatientsList(self, patientsData):
        sortedPatients = []
        patients = []

        # Object by Value
        for patientData in patientsData:
            patients.append(patientData)

        while len(patients) > 1:
            #Delete the first element as we are doing the max heap
            sortedPatients.append(patients[0])

            # Rearrange the array to perform heapify
            lastIndexPosition = len(patients) - 1
            patients[0] = patients[lastIndexPosition]

            lastIndexPosition -= 1
            patients = patients[0: lastIndexPosition + 1]

            # Perform heapify
            inputPatientsLength = len(patients) - 1
            while inputPatientsLength >= 0:
                self.heapify(inputPatientsLength, patients)
                inputPatientsLength -= 1

            # Return the data from Queue
            # patients = self.returnConsultQueue()

        sortedPatients.append(patients[0])
        return sortedPatients

    # Removes the root node from Heap
    def dequeue(self):
        # Rearrange the array to perform heapify
        lastIndexPosition = len(self.patients) - 1
        self.patients[0] = self.patients[lastIndexPosition]

        lastIndexPosition -= 1
        self.patients = self.patients[0: lastIndexPosition + 1]

        # Perform heapify
        inputPatientsLength = len(self.patients) - 1
        while inputPatientsLength >= 0:
            self.heapify(inputPatientsLength, self.patients)
            inputPatientsLength -= 1

    # Performs Heapify from the leaf nodes : O(n)
    def heapify(self, index, patients):
        # The Left child index is 2i and right child index is 2i+1
        #       As the index starts for 0, the formulae needs to adjusted as
        #       Left child index is 2i - 1 and right child index is 2i

        # Find the Left and Right Child Index
        lcIndex = 2 * (index + 1) - 1
        rcIndex =  2 * (index + 1)

        # Find the index to be swapped. Minor adjustment is needed as leaf nodes does not have children
        arrayLength = len(patients)
        indexToBeSwapped = 0

        lcIndex = -1 if lcIndex >= arrayLength else lcIndex
        rcIndex = -1 if rcIndex >= arrayLength else rcIndex

        if lcIndex == -1 and rcIndex == -1:
            return patients
        elif lcIndex == -1 or rcIndex == -1:
            indexToBeSwapped = lcIndex if lcIndex !=-1 else rcIndex
        else:
            indexToBeSwapped = lcIndex if patients[lcIndex].age >= patients[rcIndex].age else rcIndex

        # Check the values is greater or not, if  yes the swap
        # After the swap , we need to check whether the child node is satisfying
        # the heap properties, to do that we need to the same heapify
        if patients[index].age < patients[indexToBeSwapped].age:
            swap = patients[index]
            patients[index] = patients[indexToBeSwapped]
            patients[indexToBeSwapped] = swap
            array = self.heapify(indexToBeSwapped, patients)

        return patients