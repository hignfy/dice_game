// 1. Take two inputs: a datetime and a time in hours
// 2. The amount of hours reduces by 1 every hour, until it hits zero, when the date (Due Time) is printed
// 3. If a request comes in on a working day:
// 3a. If the request comes in between 9 and 17 (excl) it can start immediately.
// 3b. If the request comes in before 9, wait until 9.
// 3c. If the request comes in after 17, wait until next working day.
// 4. If the day is a saturday or sunday (aka not working days) then move onto the next day until Monday
// 5. When the reamining hours reach zero, return to step 2
// 6. Print the time elapsed (submitted date and turnaround time)


function calculateDueDate(submitDate, turnaroundTime) {
  const workingHoursStart = 9;
  const workingHoursEnd = 17;
  const workingDays = [1, 2, 3, 4, 5]; // Monday to Friday

  let dueDate = new Date(submitDate);
  let remainingHours = turnaroundTime;

  // while loop to count down the hours within the timeframe
  while (remainingHours > 0) {
    // iterate and increase time
    dueDate.setHours(dueDate.getHours() + 1);

    // set the day and hour
    let day = dueDate.getDay();
    let hour = dueDate.getHours();

    // set the working day and working hour parameters
    const isWorkingDay = workingDays.includes(day);
    const isWorkingHour = hour >= workingHoursStart && hour < workingHoursEnd; // prevents any issues with 17:00

    // point 3 - 4 in intro
    if (isWorkingDay) {
      if (isWorkingHour) {
        remainingHours--;
      } else if (hour < workingHoursStart) {
        dueDate.setHours(workingHoursStart);
      } else if (hour >= workingHoursEnd) {
        dueDate.setHours(workingHoursStart);
        dueDate.setDate(dueDate.getDate() + 1);
      }
    } else {
      do {
        dueDate.setDate(dueDate.getDate() + 1);
        day = dueDate.getDay();
      } while (!workingDays.includes(day));
      dueDate.setHours(workingHoursStart);
    }
  }

  return dueDate.toLocaleString("de-DE");
}

////////////// TESTS //////////////////

// Time inputs are ISO standard (UTC) but calculate to local time
// 1. Arrives Monday 9am and is completed same day
const mondayMorning = calculateDueDate("2023-11-06T08:00:00.000Z", 4)
console.log("Monday Prompt:  ", mondayMorning)

// 2. Arrives Tuesday before workday starts (no work before 9am)
const tuesdayEarly = calculateDueDate("2023-11-07T07:00:00.000Z", 4)
console.log("Tuesday Early: ", tuesdayEarly)

// 3. Arrives after workday ends on Wednesday (next day is a working day)
const wednesdayLate = calculateDueDate("2023-11-08T17:00:00.000Z", 4)
console.log("Wednesday Late: ", wednesdayLate)

// 4. Arrives on a Friday and continues after working time
const fridayAfternoon = calculateDueDate("2023-11-10T15:00:00.000Z", 10)
console.log("Friday Afternoon: ", fridayAfternoon)

// 5. Arrives on a Saturday
const weekendEmail = calculateDueDate("2023-11-11T01:00:00.000Z", 16)
console.log("Saturday: ", weekendEmail)

// 6. From now
const currentDate = new Date();  // Current time
const turnaroundTime = 20; // # Turnaround time
const dueDate = calculateDueDate(currentDate, turnaroundTime);

console.log('Due Date:', dueDate); // Output due date
