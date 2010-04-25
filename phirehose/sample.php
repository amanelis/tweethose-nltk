<?PHP
require_once("hose/lib/Phirehose.php");

class SampleConsumer extends Phirehose {

	public function enqueueStatus($status) {
		$data = json_decode($status, true);
		if(is_array($data) && isset($data['user']['screen_name'])) {
			print $data['user']['screen_name'].': '.urldecode($data['text'])."<br />";
		}
	}

}

$sc = new SampleConsumer('zandermane', 'alex18257', Phirehose::METHOD_SAMPLE);
$sc->consume();
