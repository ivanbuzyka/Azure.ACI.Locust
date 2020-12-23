param (
    [Parameter()]
    [string]
    $ResourceGroupName,

    [Parameter()]
    [ValidateSet('start','stop','restart')]
    [string]
    $CommandName
)

# Get all ACIs in resource group
$acis = (az container list -g $ResourceGroupName) | ConvertFrom-Json

foreach($aci in $acis) {    
    az container $CommandName --name $aci.name -g $ResourceGroupName
}