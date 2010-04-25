<?PHP

require_once('hose/lib/Phirehose.php');
class MyStream extends Phirehose
{
  public function enqueueStatus($status)
  {
    print $status;
  }
}

$stream = new MyStream('zandermane', 'alex18257');
$stream->consume();


?>
