import kue from "kue";
const queue = kue.createQueue();
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}
const someQueue = "push_notification_code";
queue.process(someQueue, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
