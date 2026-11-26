using System.Text.Json;
using TheSingularityWorkshop.FSM_API;
using TheSingularityWorkshop.FSM_API.IntegerBacked;
using IntegerFsmApi = TheSingularityWorkshop.FSM_API.IntegerBacked.FsmApi;

const int fsmId = 6100;
const int processingGroupId = 61;
const int map = 0;
const int grounds = 1;
const int gate = 2;
const int handler = 3;
const int admitted = 4;
const int challenged = 5;

var outputDirectory = args.Length > 0
    ? Path.GetFullPath(args[0])
    : Path.GetFullPath("docs/assets/generated/surps-cinematic-flow");
Directory.CreateDirectory(outputDirectory);

var definition = IntegerFsmApi.Create.CreateFiniteStateMachine(
        fsmId,
        processRate: 0,
        processingGroupID: processingGroupId)
    .State(map, onEnter: context => Enter(context, map))
    .State(grounds, onEnter: context => Enter(context, grounds))
    .State(gate, onEnter: context => Enter(context, gate))
    .State(handler, onEnter: context => Enter(context, handler))
    .State(admitted, onEnter: context => Enter(context, admitted))
    .State(challenged, onEnter: context => Enter(context, challenged))
    .WithInitialState(map)
    .Transition(map, grounds, context => ((SceneContext)context).MapConfirmed)
    .Transition(grounds, gate, context => ((SceneContext)context).GroundsReached)
    .Transition(gate, handler, context => ((SceneContext)context).HandlerRequested)
    .Transition(handler, admitted, context => ((SceneContext)context).CorrectIdentitySelected)
    .Transition(handler, challenged, context => ((SceneContext)context).WrongIdentitySelected)
    .Transition(challenged, handler, context => ((SceneContext)context).RetryRequested)
    .BuildDefinition();

IntegerFsmApi.Create.RegisterDefinition(definition);

var successContext = new SceneContext("site-k17-success");
var successHandle = IntegerFsmApi.Create.CreateInstance(fsmId, successContext);
var successTrace = RunSuccess(successHandle, successContext);
if (successHandle.CurrentStateID != admitted)
    throw new InvalidOperationException("The expected identity path did not reach the admitted state.");
IntegerFsmApi.Interaction.DestroyInstance(successHandle);

var challengeContext = new SceneContext("site-k17-challenge");
var challengeHandle = IntegerFsmApi.Create.CreateInstance(fsmId, challengeContext);
var challengeTrace = RunChallengeThenRecover(challengeHandle, challengeContext);
if (challengeHandle.CurrentStateID != admitted)
    throw new InvalidOperationException("The challenged identity path did not recover to admission.");
IntegerFsmApi.Interaction.DestroyInstance(challengeHandle);
IntegerFsmApi.Interaction.Unregister(fsmId);

var svgPath = Path.Combine(outputDirectory, "surps-cinematic-flow.svg");
var manifestPath = Path.Combine(outputDirectory, "surps-cinematic-flow.json");
await File.WriteAllTextAsync(svgPath, CreateSvg());
var manifest = new
{
    schemaVersion = 1,
    fixture = "surps.site-k17.cinematic-opening",
    runtime = "FSM_API 2.0 development · native integer-backed runtime",
    fsmId,
    processingGroupId,
    identityBacking = "integer array indexes; no string lookup in runtime path",
    states = new[]
    {
        new { id = map, name = "Map" },
        new { id = grounds, name = "Grounds" },
        new { id = gate, name = "Admission gate" },
        new { id = handler, name = "Handler instruction" },
        new { id = admitted, name = "Admitted" },
        new { id = challenged, name = "Identity challenged" }
    },
    successTrace = successTrace,
    challengeAndRecoveryTrace = challengeTrace,
    note = "Executable state-flow proof. The static HTML scene remains a separate presentation prototype."
};
await File.WriteAllTextAsync(manifestPath,
    JsonSerializer.Serialize(manifest, new JsonSerializerOptions { WriteIndented = true }) + Environment.NewLine);

Console.WriteLine($"PASS: native integer FSM {fsmId} produced success trace [{string.Join(", ", successTrace)}].");
Console.WriteLine($"PASS: native integer FSM {fsmId} produced challenge/recovery trace [{string.Join(", ", challengeTrace)}].");
Console.WriteLine($"Generated {svgPath}");
Console.WriteLine($"Generated {manifestPath}");

static void Enter(IStateContext context, int stateId)
{
    ((SceneContext)context).EnteredStates.Add(stateId);
}

static List<int> RunSuccess(FSMHandleInt handle, SceneContext context)
{
    handle.Update(); // Enter map.
    context.MapConfirmed = true;
    handle.Update(); // Map -> grounds.
    handle.Update(); // Enter grounds.
    context.GroundsReached = true;
    handle.Update(); // Grounds -> gate.
    handle.Update(); // Enter gate.
    context.HandlerRequested = true;
    handle.Update(); // Gate -> handler.
    handle.Update(); // Enter handler.
    context.CorrectIdentitySelected = true;
    handle.Update(); // Handler -> admitted.
    handle.Update(); // Enter admitted.
    return context.EnteredStates;
}

static List<int> RunChallengeThenRecover(FSMHandleInt handle, SceneContext context)
{
    handle.Update();
    context.MapConfirmed = true;
    handle.Update();
    handle.Update();
    context.GroundsReached = true;
    handle.Update();
    handle.Update();
    context.HandlerRequested = true;
    handle.Update();
    handle.Update();
    context.WrongIdentitySelected = true;
    handle.Update(); // Handler -> challenged.
    handle.Update(); // Enter challenged.
    context.WrongIdentitySelected = false;
    context.RetryRequested = true;
    handle.Update(); // Challenged -> handler.
    handle.Update(); // Re-enter handler.
    context.CorrectIdentitySelected = true;
    handle.Update(); // Handler -> admitted.
    handle.Update(); // Enter admitted.
    return context.EnteredStates;
}

static string CreateSvg()
{
    const string ink = "#e8e4d8";
    const string muted = "#aeb9b9";
    const string panel = "#17232a";
    const string line = "#72818a";
    const string gold = "#dfbd78";
    const string mint = "#76c9b3";
    const string red = "#d17d73";
    var nodes = new[]
    {
        (Id: 0, Label: "MAP", X: 90, Y: 170, Fill: panel),
        (Id: 1, Label: "GROUNDS", X: 270, Y: 170, Fill: panel),
        (Id: 2, Label: "ADMISSION", X: 450, Y: 170, Fill: panel),
        (Id: 3, Label: "HANDLER", X: 630, Y: 170, Fill: panel),
        (Id: 4, Label: "ADMITTED", X: 870, Y: 105, Fill: "#203d37"),
        (Id: 5, Label: "CHALLENGED", X: 870, Y: 245, Fill: "#402a29")
    };
    var markup = new System.Text.StringBuilder();
    markup.Append("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1080 390\" role=\"img\" aria-labelledby=\"t d\">");
    markup.Append("<title id=\"t\">Site K-17 cinematic opening — integer-backed FSM flow</title>");
    markup.Append("<desc id=\"d\">Integer state IDs 0 through 5 connect map, grounds, admission, handler, admitted, and challenged states. A challenged identity can return to the handler for recovery.</desc>");
    markup.Append("<rect width=\"1080\" height=\"390\" rx=\"18\" fill=\"#101820\"/>");
    markup.Append($"<text x=\"42\" y=\"42\" fill=\"{gold}\" font-family=\"Arial\" font-size=\"13\" letter-spacing=\"3\">SURPS · FSM_API 2.0 INTEGER-BACKED FLOW</text>");
    void Arrow(int x1, int y1, int x2, int y2, string color, string label)
    {
        markup.Append($"<path d=\"M{x1} {y1} L{x2} {y2}\" stroke=\"{color}\" stroke-width=\"3\" fill=\"none\"/>");
        markup.Append($"<path d=\"M{x2-8} {y2-6} L{x2} {y2} L{x2-8} {y2+6}\" stroke=\"{color}\" stroke-width=\"3\" fill=\"none\"/>");
        markup.Append($"<text x=\"{(x1+x2)/2}\" y=\"{(y1+y2)/2-10}\" text-anchor=\"middle\" fill=\"{muted}\" font-family=\"Arial\" font-size=\"10\">{label}</text>");
    }
    Arrow(210, 170, 270, 170, line, "map confirmed");
    Arrow(390, 170, 450, 170, line, "grounds reached");
    Arrow(570, 170, 630, 170, line, "request handler");
    Arrow(750, 160, 870, 105, mint, "correct identity");
    Arrow(750, 184, 870, 245, red, "wrong identity");
    markup.Append($"<path d=\"M930 290 L930 330 L690 330 L690 210\" stroke=\"{gold}\" stroke-width=\"2\" fill=\"none\" stroke-dasharray=\"6 5\"/>");
    markup.Append($"<path d=\"M684 220 L690 210 L696 220\" stroke=\"{gold}\" stroke-width=\"2\" fill=\"none\"/>");
    markup.Append($"<text x=\"810\" y=\"352\" text-anchor=\"middle\" fill=\"{gold}\" font-family=\"Arial\" font-size=\"10\">retry / recovery</text>");
    foreach (var node in nodes)
    {
        markup.Append($"<rect x=\"{node.X}\" y=\"{node.Y-30}\" width=\"120\" height=\"60\" rx=\"10\" fill=\"{node.Fill}\" stroke=\"{node.Id==4?mint:node.Id==5?red:line}\" stroke-width=\"2\"/>");
        markup.Append($"<text x=\"{node.X+60}\" y=\"{node.Y-3}\" text-anchor=\"middle\" fill=\"{ink}\" font-family=\"Arial\" font-size=\"11\" font-weight=\"700\">{node.Label}</text>");
        markup.Append($"<text x=\"{node.X+60}\" y=\"{node.Y+17}\" text-anchor=\"middle\" fill=\"{gold}\" font-family=\"Arial\" font-size=\"11\">STATE {node.Id}</text>");
    }
    markup.Append($"<text x=\"42\" y=\"372\" fill=\"{muted}\" font-family=\"Arial\" font-size=\"10\">Runtime state identity is integer-backed. Labels are for people; they are not runtime keys.</text></svg>");
    return markup.ToString();
}

sealed class SceneContext(string name) : IStateContext
{
    public string Name { get; set; } = name;
    public bool IsValid { get; set; } = true;
    public bool MapConfirmed { get; set; }
    public bool GroundsReached { get; set; }
    public bool HandlerRequested { get; set; }
    public bool CorrectIdentitySelected { get; set; }
    public bool WrongIdentitySelected { get; set; }
    public bool RetryRequested { get; set; }
    public List<int> EnteredStates { get; } = [];
}
