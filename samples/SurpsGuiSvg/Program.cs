using TheSingularityWorkshop.Workshop.Gui;
using TheSingularityWorkshop.Workshop.Gui.Svg;

var scene = GuiBuilder.Create("svg-scene", "surps-behavior-model")
    .Text("SURPS — one behavior model, multiple adapters")
    .Property("viewBox", "0 0 1200 760")
    .Property("aria-label", "SURPS behavior model and its tabletop and digital adapters")
    .Property("description", "An authored semantic GUI tree rendered to SVG by The Singularity Workshop GUI.SVG adapter. The diagram shows situation inputs entering one shared behavior model, which is presented through tabletop and digital adapters before changing world state.")
    .Child("svg-rect", "background", n => n
        .Property("x", "0").Property("y", "0").Property("width", "1200").Property("height", "760")
        .Property("fill", "#0b1421"))
    .Child("svg-text", "eyebrow", n => n
        .Text("SINGULARITY UNIVERSAL ROLEPLAYING SYSTEM")
        .Property("x", "64").Property("y", "62").Property("fill", "#7ee0bd")
        .Property("font-size", "18").Property("font-weight", "700").Property("letter-spacing", "3"))
    .Child("svg-text", "heading", n => n
        .Text("One behavior model. Two ways to play.")
        .Property("x", "64").Property("y", "112").Property("fill", "#edf5fc")
        .Property("font-size", "34").Property("font-weight", "700"))
    .Child("svg-text", "subtitle", n => n
        .Text("The domain meaning stays authoritative; each adapter presents it at the fidelity it can support.")
        .Property("x", "64").Property("y", "148").Property("fill", "#a8bbcf")
        .Property("font-size", "17"))
    .Child("svg-g", "input-group", n => n
        .Child("svg-rect", "input-panel", p => p
            .Property("x", "64").Property("y", "230").Property("width", "245").Property("height", "330")
            .Property("rx", "18").Property("fill", "#14263a").Property("stroke", "#38536b").Property("stroke-width", "2"))
        .Child("svg-text", "input-title", p => p.Text("SITUATION").Property("x", "88").Property("y", "274")
            .Property("fill", "#ffcf86").Property("font-size", "17").Property("font-weight", "700"))
        .Child("svg-text", "input-actor", p => p.Text("Actor").Property("x", "92").Property("y", "336")
            .Property("fill", "#edf5fc").Property("font-size", "23"))
        .Child("svg-text", "input-intent", p => p.Text("Intent").Property("x", "92").Property("y", "392")
            .Property("fill", "#edf5fc").Property("font-size", "23"))
        .Child("svg-text", "input-target", p => p.Text("Target").Property("x", "92").Property("y", "448")
            .Property("fill", "#edf5fc").Property("font-size", "23"))
        .Child("svg-text", "input-context", p => p.Text("Context + constraints").Property("x", "92").Property("y", "504")
            .Property("fill", "#a8bbcf").Property("font-size", "16")))
    .Child("svg-g", "behavior-group", n => n
        .Child("svg-rect", "behavior-panel", p => p
            .Property("x", "385").Property("y", "230").Property("width", "430").Property("height", "330")
            .Property("rx", "18").Property("fill", "#173a42").Property("stroke", "#4fba9c").Property("stroke-width", "3"))
        .Child("svg-text", "behavior-kicker", p => p.Text("AUTHORITATIVE DOMAIN MEANING").Property("x", "417").Property("y", "274")
            .Property("fill", "#7ee0bd").Property("font-size", "16").Property("font-weight", "700"))
        .Child("svg-text", "behavior-title", p => p.Text("Behavior model").Property("x", "417").Property("y", "334")
            .Property("fill", "#ffffff").Property("font-size", "31").Property("font-weight", "700"))
        .Child("svg-line", "behavior-rule", p => p.Property("x1", "417").Property("y1", "358").Property("x2", "780").Property("y2", "358")
            .Property("stroke", "#4fba9c").Property("stroke-width", "2"))
        .Child("svg-text", "behavior-state", p => p.Text("Evaluate state, capability, rules").Property("x", "417").Property("y", "404")
            .Property("fill", "#edf5fc").Property("font-size", "18"))
        .Child("svg-text", "behavior-cause", p => p.Text("Resolve causes and consequences").Property("x", "417").Property("y", "444")
            .Property("fill", "#edf5fc").Property("font-size", "18"))
        .Child("svg-text", "behavior-time", p => p.Text("Preserve time and persistent change").Property("x", "417").Property("y", "484")
            .Property("fill", "#edf5fc").Property("font-size", "18")))
    .Child("svg-g", "adapter-group", n => n
        .Child("svg-rect", "tabletop-panel", p => p.Property("x", "892").Property("y", "218").Property("width", "245").Property("height", "145")
            .Property("rx", "16").Property("fill", "#25364a").Property("stroke", "#ffcf86").Property("stroke-width", "2"))
        .Child("svg-text", "tabletop-title", p => p.Text("TABLETOP").Property("x", "918").Property("y", "262")
            .Property("fill", "#ffcf86").Property("font-size", "18").Property("font-weight", "700"))
        .Child("svg-text", "tabletop-detail", p => p.Text("Human-manageable").Property("x", "918").Property("y", "300")
            .Property("fill", "#edf5fc").Property("font-size", "17"))
        .Child("svg-text", "tabletop-detail-2", p => p.Text("derived procedure").Property("x", "918").Property("y", "328")
            .Property("fill", "#a8bbcf").Property("font-size", "16"))
        .Child("svg-rect", "digital-panel", p => p.Property("x", "892").Property("y", "426").Property("width", "245").Property("height", "145")
            .Property("rx", "16").Property("fill", "#25364a").Property("stroke", "#8fcaff").Property("stroke-width", "2"))
        .Child("svg-text", "digital-title", p => p.Text("DIGITAL").Property("x", "918").Property("y", "470")
            .Property("fill", "#8fcaff").Property("font-size", "18").Property("font-weight", "700"))
        .Child("svg-text", "digital-detail", p => p.Text("Detailed evaluation").Property("x", "918").Property("y", "508")
            .Property("fill", "#edf5fc").Property("font-size", "17"))
        .Child("svg-text", "digital-detail-2", p => p.Text("live state + cached rules").Property("x", "918").Property("y", "536")
            .Property("fill", "#a8bbcf").Property("font-size", "15")))
    .Child("svg-line", "input-to-model", n => n.Property("x1", "309").Property("y1", "395").Property("x2", "385").Property("y2", "395")
        .Property("stroke", "#7ee0bd").Property("stroke-width", "4"))
    .Child("svg-path", "model-to-adapters", n => n.Property("d", "M815 395 H850 V290 H892 M850 395 V498 H892")
        .Property("fill", "none").Property("stroke", "#7ee0bd").Property("stroke-width", "4"))
    .Child("svg-g", "outcome-group", n => n
        .Child("svg-line", "tabletop-to-outcome", p => p.Property("x1", "1014").Property("y1", "363").Property("x2", "1014").Property("y2", "616")
            .Property("stroke", "#ffcf86").Property("stroke-width", "2").Property("stroke-dasharray", "7 8"))
        .Child("svg-line", "digital-to-outcome", p => p.Property("x1", "1014").Property("y1", "571").Property("x2", "1014").Property("y2", "616")
            .Property("stroke", "#8fcaff").Property("stroke-width", "2").Property("stroke-dasharray", "7 8"))
        .Child("svg-rect", "outcome-panel", p => p.Property("x", "385").Property("y", "616").Property("width", "752").Property("height", "76")
            .Property("rx", "14").Property("fill", "#182b3d").Property("stroke", "#38536b").Property("stroke-width", "2"))
        .Child("svg-text", "outcome-title", p => p.Text("WORLD STATE CHANGES").Property("x", "417").Property("y", "662")
            .Property("fill", "#edf5fc").Property("font-size", "22").Property("font-weight", "700"))
        .Child("svg-text", "outcome-subtitle", p => p.Text("Evidence · relationships · time · consequences").Property("x", "720").Property("y", "662")
            .Property("fill", "#a8bbcf").Property("font-size", "17")))
    .Build();

var output = Path.Combine(Environment.CurrentDirectory, "docs", "assets", "generated", "surps-behavior-model.svg");
Directory.CreateDirectory(Path.GetDirectoryName(output)!);
var svg = new SvgGuiRenderer().Render(scene, width: 1200, height: 760);
File.WriteAllText(output, svg + Environment.NewLine);
Console.WriteLine($"Generated {output} ({svg.Length:N0} characters) using GUI.Core + GUI.SVG.");
