odoo.define('website_sale_snakebyte.backend.button', function (require) {
'use strict';

var AbstractField = require('web.AbstractField');
var core = require('web.core');
var field_registry = require('web.field_registry');

var _t = core._t;

var WidgetWebsitePublishButtonIcon = AbstractField.extend({
    template: 'WidgetWebsitePublishButtonIcon',
    events: {
        'click .o_button_icon,.o_stat_info': '_onClickGoto',
        'click .o_toggle_published': '_onClickToggle',
    },

    /**
    * @override
    */
    start: function () {
        this.$icon = this.$('.o_button_icon');
	this.$toggle = this.$('.o_toggle_published');
        return this._super.apply(this, arguments);
    },

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    isSet: function () {
        return true;
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _render: function () {
        this._super.apply(this, arguments);

        var published = this.value;
        var info = published ? _t("Published") : _t("Unpublished");
        this.$el.attr('aria-label', info)
                .prop('title', info);
        this.$icon.toggleClass('text-danger', !published)
                .toggleClass('text-success', published);
        this.$toggle.toggleClass('fa-square-o', !published)
                .toggleClass('fa-check-square-o', published);
    },

    //--------------------------------------------------------------------------
    // Handler
    //--------------------------------------------------------------------------

    /**
     * Redirects to the website page of the record.
     *
     * @private
     */
    _onClickGoto: function () {
        this.trigger_up('button_clicked', {
            attrs: {
                type: 'object',
                name: 'open_website_url',
            },
            record: this.record,
        });
    },

    _onClickToggle: function(){
        	this.trigger_up('button_clicked', {
        	    attrs: {
        	        type: 'object',
        	        name: 'website_publish_button',
        	    },
        	    record: this.record,
        	});
    },
});

field_registry
    .add('website_redirect_publish_button', WidgetWebsitePublishButtonIcon)
});
