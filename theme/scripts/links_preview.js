(function () {
  const tooltipWrappers = {};

  document.querySelectorAll("div.tooltip-wrapper").forEach(function (el) {
    tooltipWrappers[el.dataset["pageUrl"]] = el;
  });

  function hideTooltip(href) {
    const tooltipWrapper = tooltipWrappers[href];

    tooltipWrapper.style.display = "none";
    tooltipWrapper.style.opacity = 0;
  }

  function showTooltip(event, href) {
    const tooltipWrapper = tooltipWrappers[href];

    tooltipWrapper.style.display = "block";
    tooltipWrapper.style.opacity = 1;

    const elem = event.target;
    const elem_props = elem.getClientRects()[elem.getClientRects().length - 1];
    const top = window.pageYOffset || document.documentElement.scrollTop;

    tooltipWrapper.style.left =
      elem_props.left -
      tooltipWrapper.offsetWidth / 2 +
      elem_props.width / 2 +
      "px";

    if (window.innerHeight - elem_props.top < tooltipWrapper.offsetHeight) {
      tooltipWrapper.style.top =
        elem_props.top + top - tooltipWrapper.offsetHeight - 10 + "px";
    } else if (
      window.innerHeight - elem_props.top >
      tooltipWrapper.offsetHeight
    ) {
      tooltipWrapper.style.top = elem_props.top + top + 35 + "px";
    }

    if (
      elem_props.left + elem_props.width / 2 <
      tooltipWrapper.offsetWidth / 2
    ) {
      tooltipWrapper.style.left = "10px";
    } else if (
      document.body.clientWidth - elem_props.left - elem_props.width / 2 <
      tooltipWrapper.offsetWidth / 2
    ) {
      tooltipWrapper.style.left =
        document.body.clientWidth - tooltipWrapper.offsetWidth - 20 + "px";
    }
  }

  function setupListeners(linkElement) {
    const href = linkElement.getAttribute("href");

    linkElement.addEventListener("mouseleave", function (_event) {
      hideTooltip(href);
    });

    linkElement.addEventListener("touchend", function (_event) {
      hideTooltip(href);
    });

    linkElement.addEventListener("mouseenter", function (event) {
      showTooltip(event, href);
    });
  }

  document.querySelectorAll("a.wikilink").forEach(setupListeners);
})();
